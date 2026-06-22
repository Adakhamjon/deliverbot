import { useEffect, useState } from 'react';
import { useParams, Link } from 'react-router-dom';
import { getOrder, uploadReceipt } from '../api/api';

function OrderStatus() {
  const { id } = useParams();

  const [order, setOrder] = useState(null);
  const [receipt, setReceipt] = useState(null);

  useEffect(() => {
    getOrder(id).then(res => setOrder(res.data));

    const interval = setInterval(() => {
      getOrder(id).then(res => setOrder(res.data));
    }, 10000);

    return () => clearInterval(interval);
  }, [id]);

  const handleUpload = async () => {
    if (!receipt) {
      alert("Chek rasmini tanlang");
      return;
    }

    const formData = new FormData();
    formData.append("receipt", receipt);

    try {
      await uploadReceipt(order.id, formData);

      alert("Chek muvaffaqiyatli yuborildi");

      const res = await getOrder(order.id);
      setOrder(res.data);

    } catch (err) {
      console.error(err);
      alert("Chek yuklashda xatolik");
    }
  };

  if (!order) {
    return <div>Yuklanmoqda...</div>;
  }

  return (
    <div className="min-h-screen bg-gray-50 p-4">
      <div className="max-w-xl mx-auto bg-white rounded-xl shadow-lg p-6">

        <div className="text-center mb-6">
          <div className="text-6xl mb-3">✅</div>
          <h1 className="text-2xl font-bold">
            Buyurtmangiz qabul qilindi
          </h1>
        </div>

        <p><strong>Buyurtma raqami:</strong> #{order.id}</p>

        <p><strong>Holati:</strong> {order.status_display}</p>

        <p>
          <strong>Jami summa:</strong>{' '}
          {parseFloat(order.total).toLocaleString()} so'm
        </p>

        <hr className="my-4" />

        <h3 className="font-bold mb-2">Buyurtma tarkibi</h3>

        {order.items.map(item => (
          <div
            key={item.id}
            className="flex justify-between py-2"
          >
            <span>
              {item.menu_item_name} x {item.quantity}
            </span>

            <span>
              {(item.price * item.quantity).toLocaleString()} so'm
            </span>
          </div>
        ))}

        <hr className="my-4" />

        <div className="bg-yellow-50 border border-yellow-300 rounded-lg p-4">
          <h3 className="font-bold mb-2">
            ☎ Bog'lanish uchun
          </h3>

          <p>+998 99 392 32 09</p>
        </div>

        <div className="bg-green-50 border border-green-300 rounded-lg p-4 mt-4">

          <h3 className="font-bold mb-2">
            💳 To'lov uchun
          </h3>

          <p className="text-xl font-bold">
            9860012132929395
          </p>

          <p className="mt-2 text-sm text-gray-600">
            To'lov izohida buyurtma raqamini yozing:
            <strong> #{order.id}</strong>
          </p>

          <p className="mt-2">
            <strong>To'lov holati:</strong> {order.payment_status}
          </p>

          {order.payment_status === 'pending' && (
            <div className="mt-4">

              <input
                type="file"
                accept="image/*"
                onChange={(e) => setReceipt(e.target.files[0])}
                className="mb-2"
              />

              <button
                onClick={handleUpload}
                className="w-full bg-blue-600 text-white py-2 rounded-lg"
              >
                📤 Chek yuborish
              </button>

            </div>
          )}

        </div>

        <Link
          to="/"
          className="block text-center mt-6 bg-primary text-white py-3 rounded-lg"
        >
          Bosh sahifaga qaytish
        </Link>

      </div>
    </div>
  );
}

export default OrderStatus;