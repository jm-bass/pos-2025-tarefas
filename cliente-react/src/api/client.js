const BASE_URL = 'https://jsonplaceholder.typicode.com';

export async function getUsers() {
  const response = await fetch(`${BASE_URL}/users`);
  return response.json();
}

export async function getUser(id) {
  const response = await fetch(`${BASE_URL}/users/${id}`);
  return response.json();
}

export async function getUserPosts(userId) {
  const response = await fetch(`${BASE_URL}/posts?userId=${userId}`);
  return response.json();
}
