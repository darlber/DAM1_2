import java.util.List;

import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.hibernate.Transaction;
import org.hibernate.query.Query;
import clases.*;

public class Ejercicio1 {

	private static SessionFactory sessionFactory;

	public static void main(String[] args) {

		java.util.logging.Logger.getLogger("org.hibernate").setLevel(java.util.logging.Level.OFF);
		sessionFactory = HibernateUtil.getSessionFactory();

		System.out.println("Ejercicio 1 - Insertar Nuevas salas\r\n" + "Serradilla Gutiérrez Alberto\r\n"
				+ "=======================================");

		insertarSalas();
		mostrarListadoSalas();

		sessionFactory.close();
	}

	private static void insertarSalas() {

		Session session = sessionFactory.openSession();
		Transaction tx = null;

		try {

			tx = session.beginTransaction();

			String hql = "FROM NuevasSalas";
			Query<NuevasSalas> query = session.createQuery(hql, NuevasSalas.class);
			List<NuevasSalas> nuevassalasList = query.list();

			for (NuevasSalas nuevasSalas : nuevassalasList) {

				byte hospitalCod = nuevasSalas.getId().getHospitalCod();
				byte salaCod = nuevasSalas.getId().getSalaCod() != null ? nuevasSalas.getId().getSalaCod() : 0;
				String nombre = nuevasSalas.getId().getNombre();
				Short numCama = nuevasSalas.getId().getNumCama();

				System.out.printf("Insertando (%d, %d, %s, %d)%n", hospitalCod, salaCod, nombre, numCama);

				// inntentamos introducir los datos de nuevasSalas dentro de la tabla Salas
				// verificar si el hospital existe
				Hospitales hospital = session.get(Hospitales.class, hospitalCod);
				if (hospital == null) {
					System.out.printf("Código de hospital %d no existe, no se insertará...%n\n", hospitalCod);
					continue;
				}

				SalaId salaId = new SalaId(hospitalCod, salaCod);
				Sala existingSala = session.get(Sala.class, salaId);

				if (existingSala == null) {

					Sala sala = new Sala();
					sala.setId(salaId);
					sala.setNombre(nombre);
					sala.setNumCama(numCama);
					sala.setHospitales(hospital);

					session.persist(sala);
				} else {

					System.out.printf("Sala(%d, %d) YA EXISTE, no se insertará...%n\n", hospitalCod, salaCod);
				}
				System.out.println("Sala (" + hospitalCod + ", " + salaCod + ") " + "AÑADIDA...\n");
			}
			tx.commit();
		} finally {
			// si hay errores
			if (tx != null && tx.getStatus().canRollback()) {
				tx.rollback();
			}
			session.close();
		}
	}

	private static void mostrarListadoSalas() {

		Session session = sessionFactory.openSession();

		try {

			System.out.println("============================================================================");
			System.out.println("LISTADO DE SALAS");
			System.out.println("============================================================================");
			System.out.printf("%-23s %-20s %-6s %-10s %-10s%n", "HOSPITAL", "SALA", "CAMAS", "OCUPACIÓN", "PLANTILLA");
			System.out.println("----------------------------------------------------------------------------");

			String hql = "from Sala s join s.hospitales h order by h.hospitalCod, s.id.salaCod";
			Query<Object[]> query = session.createQuery(hql, Object[].class);
			List<Object[]> resultados = query.list();

			byte hospitalCodAnterior = -1;

			for (Object[] fila : resultados) {
				Sala sala = (Sala) fila[0];
				Hospitales hospital = (Hospitales) fila[1];

				byte hospitalCod = sala.getId().getHospitalCod();
				byte salaCod = sala.getId().getSalaCod();
				String salaNombre = sala.getNombre();
				Short numCamas = sala.getNumCama();
				String hospitalNombre = hospital.getNombre();
				long ocupacion = hospital.getOcupacions().size();
				long plantilla = hospital.getPlantillas().size();

				// salto de línea entre hospitales
				if (hospitalCod != hospitalCodAnterior && hospitalCodAnterior != -1) {
					System.out.println(); // Salto de línea entre hospitales
				}

				System.out.printf("%-2d %-18s (%-1d) %-20s %-6d %-10d %-10d%n", hospitalCod, hospitalNombre, salaCod,
						salaNombre, numCamas, ocupacion, plantilla);
				// actualizamos variable que recoge el cod par el salto de linea
				hospitalCodAnterior = hospitalCod;
			}
		} finally {
			session.close();
		}
	}
}
