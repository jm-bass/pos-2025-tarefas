import { useState, useEffect } from 'react';
import { getUserPosts } from '../api/client';

function PostList({ userId }) {
  const [posts, setPosts] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    loadPosts();
  }, [userId]);

  async function loadPosts() {
    try {
      const data = await getUserPosts(userId);
      setPosts(data);
    } catch (error) {
      console.error('Erro ao carregar posts:', error);
    } finally {
      setLoading(false);
    }
  }

  if (loading) {
    return <p>Carregando posts...</p>;
  }

  return (
    <div className="posts-section">
      <h3>Posts ({posts.length})</h3>
      <div className="posts-list">
        {posts.map(post => (
          <div key={post.id} className="post-card">
            <h4>{post.title}</h4>
            <p>{post.body}</p>
          </div>
        ))}
      </div>
    </div>
  );
}

export default PostList;
