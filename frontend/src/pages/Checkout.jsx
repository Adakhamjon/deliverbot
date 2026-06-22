import { useState } from 'react';
import { useStore } from '../store/useStore';
import { createOrder } from '../api/api';
import { useNavigate } from 'react-router-dom';
import { useEffect } from 'react';
function Checkout() {
  const { cart, getTotal, clearCart } = useStore();
  const navigate = useNavigate();
  const tg = window.Telegram?.WebApp;
  const user = tg?.initDataUnsafe?.user;
  const [form, setForm] = useState({
    customer_name: user?.first_name || '',
    phone: '',
    address: '',
    telegram_id: user?.id || null,
    telegram_username: user?.username || '',
  });

  const handleSubmit = async (e) => {
    e.preventDefault();
    
    const orderData = {
      ...form,
      telegram_id: form.telegram_id,
      telegram_username: form.telegram_username,
      items: cart.map(item => ({
        menu_item: item.id,
        quantity: item.quantity,
      })),
    };
    try {
      const res = await createOrder(orderData);
      clearCart();
      navigate(`/order/${res.data.id}`);
    } catch (err) {
      alert('Xatolik yuz berdi');
    }
  };

  return (
    <div className="checkout">
      <h1>Buyurtma</h1>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          placeholder="Ismingiz"
          value={form.customer_name}
          onChange={e => setForm({...form, customer_name: e.target.value})}
          required
        />
        <input
          type="tel"
          placeholder="Telefon"
          value={form.phone}
          onChange={e => setForm({...form, phone: e.target.value})}
          required
        />
        <textarea
          placeholder="Manzil"
          value={form.address}
          onChange={e => setForm({...form, address: e.target.value})}
          required
        />
        <h3>Jami: {getTotal().toLocaleString()} so'm</h3>
        <button type="submit">Buyurtma berish</button>
      </form>
    </div>
  );
}

export default Checkout;