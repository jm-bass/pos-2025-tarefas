import { useState, useEffect } from 'react';
import { getUsers } from '../api/client';
import UserModal from './UserModal';

function Users() {
  const [users, setUsers] = useState([]);
  const [selectedUserId, setSelectedUserId] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    loadUsers();
  }, []);

  async function loadUsers() {
    try {
      const data = await getUsers();
      setUsers(data);
    } catch (error) {
      console.error('Erro ao carregar usuários:', error);
    } finally {
      setLoading(false);
    }
  }

  function handleUserClick(userId) {
    setSelectedUserId(userId);
  }

  function handleCloseModal() {
    setSelectedUserId(null);
  }

  if (loading) {
    return <div className="loading">Carregando usuários...</div>;
  }

  return (
    <div>
      <h1>Usuários - JSONPlaceholder</h1>
      <div className="users-grid">
        {users.map(user => (
          <div 
            key={user.id} 
            className="user-card"
            onClick={() => handleUserClick(user.id)}
          >
            <h2>{user.name}</h2>
            <p><strong>Email:</strong> {user.email}</p>
            <p><strong>Empresa:</strong> {user.company.name}</p>
            <p className="click-hint">Clique para ver posts</p>
          </div>
        ))}
      </div>
      {selectedUserId && (
        <UserModal 
          userId={selectedUserId} 
          onClose={handleCloseModal}
        />
      )}
    </div>
  );
}

export default Users;
