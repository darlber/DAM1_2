import java.util.Iterator;
import java.util.List;

import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.hibernate.Transaction;

import clases.*;
import org.hibernate.query.Query;

public class Ejercicio2 {

	private static SessionFactory sessionFactory;

	public static void main(String[] args) {

		java.util.logging.Logger.getLogger("org.hibernate").setLevel(java.util.logging.Level.OFF);
		sessionFactory = HibernateUtil.getSessionFactory();

		System.out.println("Ejercicio 2 - Insertando-Actualizando Resumen Hospitales\n"
				+ "Serradilla Gutiérrez Alberto\r\n" + "=======================================");

		actualizarHospital();
		mostrarListado();
		sessionFactory.close();

	}

	private static void actualizarHospital() {
		Session session = sessionFactory.openSession();
		Transaction tx = null;

		try {
			tx = session.beginTransaction();

			// buscamos todos los hospitales que existen
			String hql = "FROM Hospitales";
			Query<Hospitales> query = session.createQuery(hql, Hospitales.class);
			List<Hospitales> listaHospitales = query.list();

			for (Hospitales h : listaHospitales) {
				// cada hospital tendra su codigo y sus ocupaciones por lo que, obtenemos
				// primero los datos
				Byte hospitalCod = h.getHospitalCod();
				short numSalas = (short) h.getSalas().size();
				short numEnfermos = (short) h.getOcupacions().size();
				short numDoctores = (short) h.getDoctors().size();
				short numPlantillas = (short) h.getPlantillas().size();

				ResumenHospitales resumen = session.get(ResumenHospitales.class, hospitalCod);

				if (resumen == null) {
					resumen = new ResumenHospitales();
					resumen.setHospitales(h);
					resumen.setNumDoctores(numDoctores);
					resumen.setNumSalas(numSalas);
					resumen.setNumEnfermos(numEnfermos);
					resumen.setNumPlantilla(numPlantillas);

					session.persist(resumen);
					System.out.println("Hospital Cod (" + hospitalCod + ") AÑADIDO...");
				} else {
					// actualizamos los totales
					resumen.setNumDoctores((short) (resumen.getNumDoctores() + numDoctores));
					resumen.setNumSalas((short) (resumen.getNumSalas() + numSalas));
					resumen.setNumEnfermos((short) (resumen.getNumEnfermos() + numEnfermos));
					resumen.setNumPlantilla((short) (resumen.getNumPlantilla() + numPlantillas));

					session.merge(resumen);
					System.out.println("Hospital Cod (" + hospitalCod + ") YA EXISTE, se actualiza...");
				}
			}

			tx.commit();
		} catch (Exception e) {
			if (tx != null)
				tx.rollback();
			e.printStackTrace();
		} finally {
			session.close();
		}
	}

	private static void mostrarListado() {

		Session session = sessionFactory.openSession();

		try {

			System.out.println("============================================================================");
			System.out.println("LISTADO DE SALAS");
			System.out.println("============================================================================");
			System.out.printf("%-23s %-20s %-6s %-10s %-10s%n", "HOSPITAL", "DOCTORES", "ENFERMOS", "PLANTILLA",
					"SALAS");
			System.out.println("----------------------------------------------------------------------------");

			String hql = "from ResumenHospitales h order by h.hospitalCod";
			Query<Object[]> query = session.createQuery(hql, Object[].class);
			List<Object[]> resultados = query.list();

			for (Object[] fila : resultados) {
				ResumenHospitales rh = (ResumenHospitales) fila[0];
				byte hospitalCod = rh.getHospitalCod();
				long totalDoc = rh.getNumDoctores();
				long totalEnf = rh.getNumEnfermos();
				long plantilla = rh.getNumPlantilla();
				long numSalas = rh.getNumSalas();
				Hospitales h = session.get(Hospitales.class, hospitalCod);
				String hospitalName = h.getNombre();

				System.out.printf("(%-2d) %-18s %-20d %-10d %-10d %-10d \n", hospitalCod, hospitalName, totalDoc,
						totalEnf, plantilla, numSalas);

			}
		} finally {
			
				session.close();
		}
	}
}