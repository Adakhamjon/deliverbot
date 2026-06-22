import axios from 'axios';

const API_URL = '/api';

export const api = axios.create({
  baseURL: API_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Kategoriyalar
export const getCategories = () => api.get('/categories/');

// Menyu
export const getMenuItems = (categoryId) => {
  const params = categoryId ? { category: categoryId } : {};
  return api.get('/menu-items/', { params });
};

// Buyurtma
export const createOrder = (data) => api.post('/orders/', data);
export const getOrder = (id) => api.get(`/orders/${id}/`);
export const uploadReceipt = (id, formData) =>
  api.post(
    `/orders/${id}/upload_receipt/`,
    formData,
    {
      headers: {
        'Content-Type': 'multipart/form-data'
      }
    }
  );