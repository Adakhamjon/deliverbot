import { create } from 'zustand';

export const useStore = create((set, get) => ({
  // Kategoriyalar
  categories: [],
  setCategories: (categories) => set({ categories }),
  
  // Menyu
  menuItems: [],
  setMenuItems: (menuItems) => set({ menuItems }),
  
  // Savat
  cart: [],
  addToCart: (item) => {
    const cart = get().cart;
    const existing = cart.find(i => i.id === item.id);
    
    if (existing) {
      set({
        cart: cart.map(i => 
          i.id === item.id 
            ? { ...i, quantity: i.quantity + 1 } 
            : i
        )
      });
    } else {
      set({ cart: [...cart, { ...item, quantity: 1 }] });
    }
  },
  
  removeFromCart: (id) => {
    set({ cart: get().cart.filter(i => i.id !== id) });
  },
  
  updateQuantity: (id, quantity) => {
    if (quantity <= 0) {
      get().removeFromCart(id);
      return;
    }
    set({
      cart: get().cart.map(i => 
        i.id === id ? { ...i, quantity } : i
      )
    });
  },
  
  clearCart: () => set({ cart: [] }),
  
  // Jami summa
  getTotal: () => {
    return get().cart.reduce((sum, item) => sum + item.price * item.quantity, 0);
  },
}));