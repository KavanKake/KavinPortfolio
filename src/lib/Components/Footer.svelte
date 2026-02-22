<script>
  import { t } from "$lib/i18n";
</script>

<footer class="footer">
  <svg
    viewBox="0 0 1440 120"
    preserveAspectRatio="none"
    class="footer-wave"
  >
    <polyline
      points="0,40 400,10 800,70 1200,60 1440,30"
      fill="none"
      stroke="#3066BE"
      stroke-width="4"
    />
  </svg>

  <div class="footer-content">
    <div class="left">
      <h2>KAVIN LOKESWARAN</h2>
      <h3>{$t("footer_social")}</h3>
      <ul>
        <li>Instagram - kavinlokeswaran</li>
        <li>LinkedIn - kavinlokeswaran</li>
        <li>GitHub - kavinlokeswaran</li>
        <li>Twitter - kavinlokeswaran</li>
      </ul>
      <a href="#top" class="back-to-top">{$t("footer_back_to_top")}</a>
    </div>
    <div class="right">
      <h3>{$t("footer_nav")}</h3>
      <nav>
        <a href="/">{$t("footer_home")}</a>
        <a href="/projects">{$t("footer_projects")}</a>
        <a href="/aboutme">{$t("footer_about")}</a>
        <a href="/contactme">{$t("footer_contact")}</a>
      </nav>
      <p class="copyright">{$t("footer_copyright")}</p>
    </div>
  </div>
</footer>


<style>
.footer {
  position: relative;
  background: #030027;
  color: #3066BE;
  padding-top: 6rem;
  padding-bottom: 2rem;
  font-family: "alphabet-soup-pro", sans-serif;
}

.footer-wave {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 120px;
}

.footer-content {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  padding: 0 6rem;
  gap: 3rem;
  flex-wrap: wrap;
}

.left h2 {
  font-size: 3rem;
  margin-bottom: 1rem;
}

.left h3,
.right h3 {
  font-size: 2rem;
  margin-bottom: 1rem;
}

.left ul {
  list-style: none;
  padding: 0;
  margin-bottom: 1.5rem;
  font-family: "alphabet-soup-pro", sans-serif;
    font-size: 1.5rem;

}

.left li {
  margin-bottom: 0.5rem;
  font-family: "alphabet-soup-pro", sans-serif;
}

.back-to-top {
  text-decoration: none;
  color: #3066BE;
  font-weight: 600;
  font-size: larger;
  border: #3066BE 2px solid;
  border-radius: 10px;
  padding: 10px;
}

.right nav {
  display: flex;
  flex-direction: column;
  gap: 0.6rem;
  margin-bottom: 3rem;
  font-size: larger;
}

.right nav a {
  text-decoration: none;
  color: #3066BE;
  font-family: "alphabet-soup-pro", sans-serif;
    font-weight: 500;
    font-size: 1.5rem;
}

.copyright {
  font-size: 0.9rem;
  opacity: 0.7;
}

@media (max-width: 900px) {
  .footer-content {
    flex-direction: column;
    padding: 0 2rem;
    align-items: flex-start;
  }

  .left h2 {
    font-size: 2.2rem;
  }

  .left h3,
  .right h3 {
    font-size: 1.6rem;
  }

  .right nav {
    flex-direction: row;
    flex-wrap: wrap;
    gap: 0.75rem 1.5rem;
  }

  .right nav a {
    font-size: 1.1rem;
  }
}

@media (max-width: 600px) {
  .footer {
    padding-top: 4rem;
    padding-bottom: 1.5rem;
  }

  .footer-content {
    padding: 0 1.5rem;
  }

  .left ul {
    font-size: 1.1rem;
  }

  .back-to-top {
    display: inline-block;
    margin-top: 0.75rem;
  }
}

</style>