import java.util.List;

import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.hibernate.query.Query;

public class Ejercicio4 {
	private static SessionFactory sessionFactory;

	public static void main(String[] args) {

		java.util.logging.Logger.getLogger("org.hibernate").setLevel(java.util.logging.Level.OFF);
		sessionFactory = HibernateUtil.getSessionFactory();

		System.out.println("Ejercicio 4 - CONSULTAS\r\n" + "Serradilla Gutiérrez Alberto\r\n"
				+ "=======================================");

		consultas();
		sessionFactory.close();

	}

	private static void consultas() {
		/*
		 * Consulta1: Consulta que muestre la siguiente información de los hospitales
		 * que tienen plantilla: Cod de Hospital, Nombre de hospital, Nº empleados
		 * plantilla, Salario medio
		 * 
		 * Consulta2: Consulta que muestre el nombre del hospital con mayor plantilla,
		 * su código y la plantilla: Cod de Hospital, Nombre de hospital, Nº empleados
		 * plantilla
		 * 
		 * Consulta3: Consulta que muestre el nombre de los hospitales que no tienen
		 * plantilla.
		 * 
		 * Consulta4: Consulta que muestre el apellido de los enfermos que están
		 * ocupando las salas de los hospitales. Se debe mostrar el nombre del hospital,
		 * nombre de la sala, apellido del enfermo y la cama que ocupa, ordenado el
		 * listado por nombre del hospital
		 * 
		 */
		Session session = sessionFactory.openSession();
		String hql = """
				SELECT
				h.hospitalCod,
				h.nombre,
				COUNT(p.empleadoNo),
				AVG(p.salario)
				FROM Hospitales h
				JOIN h.plantillas p
				GROUP BY h.hospitalCod, h.nombre
				ORDER BY
				h.hospitalCod
				""";
		Query<Object[]> query = session.createQuery(hql, Object[].class);
		List<Object[]> resultados = query.list();
		System.out.println("Consulta1");

		if (!resultados.isEmpty()) {
			for (Object[] fila : resultados) {

				Byte hospitalCod = (Byte) fila[0];
				String nombre = (String) fila[1];
				Long totalEmpleados = (Long) fila[2];
				Double salarioPromedio = (Double) fila[3];

				System.out.println("Código del Hospital: " + hospitalCod);
				System.out.println("Nombre del Hospital: " + nombre);
				System.out.println("Total de Empleados: " + totalEmpleados);
				System.out.printf("Salario Promedio: %.2f\n", salarioPromedio);
				System.out.println("-----------------------------------");
			}
		}
		System.out.println("\nConsulta2");
		String hql2 = """
				  SELECT h.hospitalCod, h.nombre, COUNT(p.empleadoNo) as numEmpleados
				  FROM Hospitales h
				  JOIN h.plantillas p
				  GROUP BY h.hospitalCod, h.nombre
				  ORDER BY numEmpleados DESC
				""";

		Query<Object[]> query2 = session.createQuery(hql2, Object[].class);
		query2.setMaxResults(1);
		List<Object[]> resulta2 = query2.list();

		if (!resulta2.isEmpty()) {
			Object[] fila = resulta2.get(0);
			Byte hospitalCod = (Byte) fila[0];
			String nombre = (String) fila[1];
			Long numEmpleados = (Long) fila[2];

			System.out.println("Código del Hospital: " + hospitalCod);
			System.out.println("Nombre del Hospital: " + nombre);
			System.out.println("Número de Empleados en la Plantilla: " + numEmpleados);
		}
		System.out.println("-----------------------------------");
		System.out.println("\nConsulta3");

		String hql3 = """
				SELECT h.nombre
				FROM Hospitales h
				LEFT JOIN h.plantillas p
				WHERE p.empleadoNo IS NULL
				""";

		Query<String> query3 = session.createQuery(hql3, String.class);
		List<String> resultres = query3.list();
		if (!resultres.isEmpty()) {

			System.out.println("Los siguientes hospitales no tienen plantilla: ");
			for (String hospitalNombre : resultres) {
				System.out.println(hospitalNombre);
			}
		}

		System.out.println("-----------------------------------");
		System.out.println("\nConsulta4");

		String hql4 = """
				   SELECT h.nombre, s.nombre, e.apellido, o.cama
				   FROM Hospitales h
				   JOIN h.salas s
				   JOIN s.ocupacions o
				   JOIN o.enfermo e
				   ORDER BY h.nombre
				""";
		Query<Object[]> query4 = session.createQuery(hql4, Object[].class);
		List<Object[]> resulcuatro = query4.list();
		if (!resulcuatro.isEmpty()) {
			for (Object[] fila : resulcuatro) {

				String hospitalNombre = (String) fila[0];
				String salaNombre = (String) fila[1];
				String apellidoEnfermo = (String) fila[2];
				Short cama = (Short) fila[3];

				System.out.println("Hospital: " + hospitalNombre);
				System.out.println("Sala: " + salaNombre);
				System.out.println("Enfermo: " + apellidoEnfermo);
				System.out.println("Cama: " + cama);
				System.out.println("-----------------------------------");
			}

		}
		session.close();
	}
}
