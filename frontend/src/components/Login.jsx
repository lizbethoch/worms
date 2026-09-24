import '../App.css'

function Login() {
  return (
    <main className="login-page">
      <section className="login-card">
        <h1>Worms</h1>

        <p>Your reading life, in one place.</p>

        <form>
          <label htmlFor="email">Email</label>
          <input
            id="email"
            type="email"
            placeholder="Enter your email"
          />

          <label htmlFor="password">Password</label>
          <input
            id="password"
            type="password"
            placeholder="Enter your password"
          />

          <button type="submit">
            Log In
          </button>
        </form>

        <p>
          Don't have an account? <a href="#">Create one</a>
        </p>
      </section>
    </main>
  )
}

export default Login