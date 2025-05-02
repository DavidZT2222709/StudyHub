import { useAuth } from '../context/AuthContext';

export default function Dashboard() {
  const { user } = useAuth();

  return (
    <div className="container mt-5">
      <h2>Bienvenido {user?.username}</h2>
      <p>Rol: {user?.rol}</p>
    </div>
  );
}
