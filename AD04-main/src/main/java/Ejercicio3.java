import java.util.List;
import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.hibernate.query.Query;

import clases.*;

public class Ejercicio3 {

	private static SessionFactory sessionFactory;

	public static void main(String[] args) {

		java.util.logging.Logger.getLogger("org.hibernate").setLevel(java.util.logging.Level.OFF);
		sessionFactory = HibernateUtil.getSessionFactory();

		System.out.println("Ejercicio 3 - LISTADO DE HOSPITALES\r\n" + "Serradilla Gutiérrez Alberto\r\n"
				+ "=======================================");

		mostrarListado();
		sessionFactory.close();

	}

	private static void mostrarListado() {
		Session session = sessionFactory.openSession();

		try {

			String hql = "FROM Hospitales h LEFT JOIN h.salas s LEFT JOIN s.plantillas p ORDER BY h.hospitalCod, s.id.salaCod";
			Query<Object[]> query = session.createQuery(hql, Object[].class);
			List<Object[]> resultados = query.list();

			// necesitamos hospitales, salas, plantilla.apellidos plantilla.salario long
			// las siguientes variables sirven para las cabeceras y los system.out
			int lastHospitalCod = -1;
			int lastSalaCod = -1;
			boolean salaConPlantilla = false;

			for (int i = 0; i < resultados.size(); i++) {
				Object[] fila = resultados.get(i);
				Hospitales h = (Hospitales) fila[0];
				Sala s = (Sala) fila[1];
				Plantilla p = (Plantilla) fila[2];

				if (h != null) {
					byte hospitalCod = h.getHospitalCod();
					String hospNombre = h.getNombre();
					String hospitalDirec = h.getDireccion();
					int numCamas = h.getNumCama();

					if (s == null) {
						// si no tiene salas, saltamos al siguiente hospital
						continue;
					}

					if (hospitalCod != lastHospitalCod) {
						if (lastHospitalCod != -1) {

							String hqlSalario = "SELECT AVG(p.salario) FROM Hospitales h JOIN h.plantillas p where h.hospitalCod = :hospCod";
							Query<Double> querySalario = session.createQuery(hqlSalario, Double.class);
							querySalario.setParameter("hospCod", lastHospitalCod);

							List<Double> salarios = querySalario.list();

							for (Double salario : salarios) {

								System.out.printf("\nSalario Medio del Hospital: %.2f\n", salario);
								System.out.println(
										"-----------------------------------------------------------------------");
							}
						}

						// cabecera hospital
						System.out.printf("COD-HOSPITAL: %-2d NOMBRE: %-20s\n", hospitalCod, hospNombre);
						System.out.printf("DIRECCIÓN: %-20s Número de camas del hospital: %-3d\n", hospitalDirec,
								numCamas);
						System.out.printf("-----------------------------------------------------------------------");

						lastHospitalCod = hospitalCod;
					}

					if (s != null) {
						int salaCod = s.getId().getSalaCod();

						if (salaCod != lastSalaCod) {
							System.out.println("\nSALA NOMBRE                APELLIDO           SALARIO");
							System.out.println("==== ==================== ================== ==========");
							System.out.printf("%-4d %-21s", s.getId().getSalaCod(), s.getNombre());
							lastSalaCod = salaCod;
							salaConPlantilla = false;

						} else {
							System.out.printf("%-4s %-21s", "", "");
						}

						if (p != null) {
							String planNombre = p.getApellido();
							double planSalario = p.getSalario();
							System.out.printf("%-18s %10.2f\n", planNombre, planSalario);
							salaConPlantilla = true;
						} else {
							System.out.println("LA SALA NO TIENE PLANTILLA\n");
						}
					}

					/*
					 * El siguiente if trata de verificar dos condiciones:
					 * 
					 * 1. Si la sala tiene plantilla asociada (salaConPlantilla).
					 * 2. Si la plantilla mostrada es la última de la lista de resultados (i == resultados.size() - 1), 
					 * 
					 * 3. Si no es la última plantilla,
					 * 3.1 Es nulo? o 3.2El siguiente elemento en la lista  es nulo? (resultados.get(i + 1)[1]).
					 * 3.3 El código de la sala siguiente es distinto a la actual? - El código de la sala en el siguiente elemento sea diferente al código de la sala actual
					 * (resultados.get(i + 1)[1]) != (s.getId().getSalaCod())
					 */
					
					if (salaConPlantilla && (i == resultados.size() - 1 || (s != null
							&& resultados.get(i + 1)[1] != null
							&& ((Sala) resultados.get(i + 1)[1]).getId().getSalaCod() != s.getId().getSalaCod()))) {

						String hqlSalarioplan = "SELECT AVG(p.salario) FROM Sala s JOIN s.plantillas p WHERE s.hospitales.hospitalCod = :hospCod AND s.id.salaCod = :salaCod";
						Query<Double> hqlPlantilla = session.createQuery(hqlSalarioplan, Double.class);

						hqlPlantilla.setParameter("hospCod", lastHospitalCod);
						hqlPlantilla.setParameter("salaCod", lastSalaCod);

						List<Double> salariosPlan = hqlPlantilla.list();

						for (Double salariop : salariosPlan) {
							System.out.printf("%55s\n", "------------------ ----------");
							System.out.printf("%41s %5s %.2f\n", "Salario medio: ", "", salariop);
						}
					}
				}
			}

		} finally {
			if (session != null) {
				session.close();
			}
		}
	}
}
