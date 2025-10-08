# 🛍️ Shop@JP

![Python](https://img.shields.io/badge/python-3.11-blue)
![Django](https://img.shields.io/badge/django-5.2-green)
![MySQL](https://img.shields.io/badge/mysql-8.0-orange)
![Stripe](https://img.shields.io/badge/stripe-payments-purple)
![Ngrok](https://img.shields.io/badge/ngrok-local%20webhook-blueviolet)
![SMTP](https://img.shields.io/badge/email-OTP%20verification-yellow)
![License](https://img.shields.io/badge/license-MIT-blue)
![Issues](https://img.shields.io/github/issues/6jp9/Shop-at-JP)


**Shop@JP (Django, Python, MySQL, Stripe API, HTML, CSS, Bootstrap, JavaScript, SMTP)**  
A full-stack e-commerce platform for merchants and customers featuring secure Stripe payments, OTP email verification, order management, refunds, and responsive UI.

---

## 🚀 Features

- ✅ Customer & Merchant registration  
- 🔐 Email verification via OTP (SMTP)  
- 🛒 Product listing, cart & checkout  
- 💳 Stripe payment integration with metadata  
- 🔁 Refund & cancellation system  
- 📈 Merchant revenue tracking  
- 📬 Stripe Webhooks for payment confirmation  
- 📊 Admin dashboard for managing users & orders  
- 📱 Responsive UI (Bootstrap 5)

---

## ⚙️ Technologies Used

| Category | Technologies |
|-----------|--------------|
| **Backend** | Django, Python |
| **Frontend** | HTML, CSS, Bootstrap, JavaScript |
| **Database** | MySQL |
| **Payment Gateway** | Stripe API with Webhooks |
| **Email Service** | SMTP (OTP verification) |
| **Testing / Local Webhooks** | Ngrok |

---

## 🧩 Installation & Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/6jp9/Shop-at-JP.git
   ```
2. Navigate into the project folder:
   ```bash
   cd Shop-at-JP
   ```
3. **Create a virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   ```
4. Activate the virtual environment:
   - Windows: `venv\Scripts\activate`  
   - Mac/Linux: `source venv/bin/activate`
5. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
6. Configure **MySQL** credentials and **SMTP** settings in `settings.py`.
7. Apply migrations:
   ```bash
   python manage.py migrate
   ```
8. **Stripe Setup for Test Mode**:
   1. Go to your [Stripe Dashboard](https://dashboard.stripe.com/test/dashboard).  
   2. Navigate to **Developers → API Keys**.  
   3. Copy your **Publishable key** and **Secret key**.  
   4. Add these keys to your Django `settings.py`:
      ```python
      STRIPE_PUBLISHABLE_KEY = "your-publishable-key"
      STRIPE_SECRET_KEY = "your-secret-key"
      ```

9. **Ngrok setup for Stripe Webhooks**:
   - Download Ngrok from [https://ngrok.com/](https://ngrok.com/) and sign up for a free account if you don’t have one.  
   - Start a tunnel to your Django server:
     ```bash
     ngrok http 8000
     ```
   - Copy the **HTTPS URL** provided by Ngrok (e.g., `https://abcd1234.ngrok.io`)  

10. **Stripe Webhook endpoint setup**:
    1. Go to [Stripe Webhooks](https://dashboard.stripe.com/test/webhooks).  
    2. Click **“+ Add endpoint”** and paste your Ngrok HTTPS URL followed by your webhook path, e.g.:
       ```
       https://abcd1234.ngrok.io/stripe/webhook/
       ```
       *(Path must match the one configured in your Django `urls.py` for webhook.)*  
    3. Select the events to listen for (at minimum: `checkout.session.completed` and `charge.refunded`).  
    4. Click **Add endpoint**.  
    5. Copy the **Signing Secret** and add it to Django `settings.py` as `STRIPE_WEBHOOK_SECRET`.

11. Run your Django server:
    ```bash
    python manage.py runserver
    ```
12. Create a Django superuser to access the admin dashboard:
    ```bash
    python manage.py createsuperuser
    ```
    - Enter a username, email, and password when prompted.
    - After this, you can log in at `http://127.0.0.1:8000/admin/` to manage users, orders, and products.


Your Stripe payments and refunds will now be processed locally through Ngrok and handled by your webhook view.

---

## 🧠 Usage

- Sign up as a **Customer** or **Merchant**.  
- Verify your account using **OTP sent via email** (SMTP).  
- Merchants can **add products, manage inventory, and track revenue**.  
- Customers can **browse products, add to cart, and checkout**.  
- Payments are securely processed through **Stripe**.  
- Use this **test card** during development:  
  ```
  4242 4242 4242 4242
  Expiry: Any future date (e.g., 12/34)
  CVC: Any 3 digits (e.g., 123)
  ```
- **Webhooks** (via Ngrok) automatically update order and payment details.  
- **Refunds** reflect instantly on both customer and merchant dashboards.

---

## 🗃️ Database Models

| Model | Description |
|--------|--------------|
| **Customer** | Stores user details & verified email |
| **Merchant** | Stores merchant info & total revenue |
| **Product** | Product info, stock, pricing |
| **Cart** | Customer cart items |
| **Order** | Order details & status |
| **Payment** | Payment data, fees, refunds, timestamps |

---

## 💰 Payment & Refund Workflow

1. Stripe Checkout Session created on payment.  
2. Metadata stores `cart_id` for backend order mapping.  
3. Stripe Webhooks confirm successful payments (Ngrok used for local testing).  
4. Order & payment models updated automatically.  
5. Refunds can be triggered manually or via Webhook.  
6. Merchant revenue adjusts after each refund.

---

## 🔑 API Access (Optional)

- To access the product API via Postman or other tools, you need an **authentication token**.
- Only an **admin user** can create a token for users.
- Steps to generate a token:
  1. Log in to the Django admin panel: `http://127.0.0.1:8000/admin/`
  2. Go to the **Users** section and select a user.
  3. Create a **Token** for the user (requires `django-rest-framework` and `rest_framework.authtoken` installed and configured).
  4. Use this token in the **Authorization header** in Postman: `http://127.0.0.1:8000/api/`
     ```
     Authorization: Token <user-token>
     ```
- This token allows authenticated access to your product API endpoints.

---

## 🖼️ Screenshots

![Home](<./screenshots/Screenshot (189).png>)
![User Sign-Up](<./screenshots/Screenshot (190).png>) 
![Merchant Profile](<./screenshots/Screenshot (191).png>) 
![Merchant Dashboard](<./screenshots/Screenshot (192).png>) 
![Cart](<./screenshots/Screenshot (193).png>) 
![Buy Phase](<./screenshots/Screenshot (195).png>)
![Checkout](<./screenshots/Screenshot (194).png>) 

---

## 📦 Future Enhancements

- 🔒 Customer password change & account settings
- ⭐ Customer product reviews & ratings
- 🎨 Better UI / UX enhancements
- 🤖 AI Chatbot for customer support
- 💰 Merchant revenue checkout (transfer to bank)
- 🚚 Order tracking
- 📦 Wishlist & favorites
- 🔔 Email / push notifications for order updates
- 🛍️ Promotions & discount codes
- 🔄 Multi-currency support
- 📊 Analytics dashboard for merchants

---

## 🤝 Contributing

1. Fork the repo  
2. Create a branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit changes:
   ```bash
   git commit -m "Add new feature"
   ```
4. Push the branch:
   ```bash
   git push origin feature-name
   ```
5. Open a Pull Request  

---

## 📜 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

### 🌐 Connect
For queries or feedback:  
📧 Email: [Jaya Prakash](mailto:jayaprakash.peddi619@gmail.com)  
Created by [Jaya Prakash](https://github.com/6jp9)  
Made with ❤️ using Django + Stripe API + Ngrok
