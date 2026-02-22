<script>
  import Footer from "$lib/Components/Footer.svelte";
  import { t } from "$lib/i18n";
  import ScrollReveal from "$lib/Components/ScrollReveal.svelte";
</script>

<main class="contact-page">
  <div class="spacer"></div>
  <div class="frontpage">
    <div class="section_1">
      <ScrollReveal>
        <h1>{$t("contact_heading")}</h1>
        <h3>{$t("contact_intro1")}</h3>
        <h3>{$t("contact_intro2")}</h3>
        <div class="email">
          <img class="mail_logo" src="/assets/mail.png" alt="" />
          <h3>contact@kavinlokeswaran.no</h3>
        </div>
      </ScrollReveal>
    </div>
    <ScrollReveal delay={150}>
      <div class="section_2">
        <h2 class="contactform">{$t("contact_form_title")}</h2>
        <form
          method="POST"
          action="https://formsubmit.co/contact@kavinlokeswaran.no"
        >
          <input type="hidden" name="_subject" value={$t("contact_subject_hidden")} />
          <label class="name" for="firstname">{$t("contact_name")}</label>
          <div class="nameSplit">
            <input id="firstname" name="Navn" type="text" class="placeholderName" placeholder={$t("contact_firstname")} required />
            <input name="Etternavn" type="text" class="placeholderName" placeholder={$t("contact_lastname")} />
          </div>
          <label class="name" for="email">{$t("contact_email")}</label>
          <input id="email" name="Email" type="email" class="placeholder" placeholder={$t("contact_email_placeholder")} required />
          <label class="name" for="topic">{$t("contact_topic")}</label>
          <input id="topic" name="Emne" type="text" class="placeholder" placeholder={$t("contact_topic_placeholder")} />
          <label class="name" for="message">{$t("contact_message")}</label>
          <textarea id="message" name="Melding" placeholder={$t("contact_message_placeholder")}></textarea>
          <button class="submit" type="submit">{$t("contact_submit")}</button>
        </form>
      </div>
    </ScrollReveal>
  </div>
  <div class="footer-spacer"></div>
  <Footer />
</main>
    
<style>
  .contact-page {
    background-color: #030027;
    min-height: 100vh;
    font-family: "coolvetica", sans-serif;
    font-weight: 400;
  }

  :global(body.dark-mode) .contact-page {
    background-color: #0d0c1d;
  }

  .spacer {
    height: 12em;
  }

  .footer-spacer {
    height: 4em;
  }

  .frontpage {
    display: flex;
    flex-direction: row;
    gap: 10em;
    overflow-x: hidden;
    margin-left: 0;
    justify-content: center;
    align-items: flex-start;
    padding: 0 2rem 2rem;
  }

  .section_1 {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: center;
    margin-top: 5em;
    padding-left: 3em;
  }

  .section_2 {
    display: flex;
    flex-direction: column;
    justify-content: center;
    text-align: center;
    border: 10px solid #024d98;
    border-radius: 20px;
    padding: 1.5em;
    margin-top: 3em;
    margin-bottom: 2em;
    height: fit-content;
    width: 35em;
    max-width: 95vw;
    background: rgba(255, 255, 255, 0.03);
  }

  :global(body.dark-mode) .section_2 {
    background: rgba(0, 0, 0, 0.2);
    border-color: #3066be;
  }

  .contactform {
    font-family: "alphabet-soup-pro", sans-serif;
    color: #024d98;
    font-size: 1.75em;
    font-weight: 500;
    margin: 0 0 0.5em;
  }

  :global(body.dark-mode) .contactform {
    color: #6fa3ff;
  }

  form {
    display: flex;
    text-align: left;
    flex-direction: column;
    gap: 0.5em;
  }

  textarea {
    height: 10em;
    border-radius: 10px;
    font-family: inherit;
    font-size: 1em;
    padding: 1em;
    border: 2px solid #3066be;
    background: #030027;
    color: #eee;
  }

  :global(body.dark-mode) textarea {
    background: #1a1a2e;
    border-color: #3066be;
  }

  .name {
    padding-top: 0.5em;
    font-size: 0.95rem;
    font-weight: 500;
    color: #3066be;
  }

  :global(body.dark-mode) .name {
    color: #9ab8ff;
  }

  .submit {
    display: flex;
    justify-content: center;
    align-items: center;
    margin-top: 1em;
    font-family: inherit;
    font-size: 1em;
    padding: 0.6em 1.2em;
    border-radius: 10px;
    border: none;
    color: white;
    background-color: #024d98;
    width: 10em;
    cursor: pointer;
    transition: transform 0.2s, background-color 0.2s;
  }

  .submit:hover {
    background-color: #3066be;
    transform: scale(1.05);
  }

  .placeholder,
  .placeholderName {
    font-family: inherit;
    font-size: 1em;
    padding: 1em;
    border-radius: 10px;
    border: 2px solid #3066be;
    background: #030027;
    color: #eee;
  }

  .placeholderName {
    width: 100%;
    box-sizing: border-box;
  }

  :global(body.dark-mode) .placeholder,
  :global(body.dark-mode) .placeholderName {
    background: #1a1a2e;
    border-color: #3066be;
    color: #eee;
  }

  .mail_logo {
    width: 2em;
    height: auto;
    margin-right: 0.5em;
    filter: brightness(0) invert(1);
  }

  .contact-page h1 {
    color: #024d98;
    font-family: "alphabet-soup-pro", sans-serif;
  }

  :global(body.dark-mode) .contact-page h1 {
    color: #6fa3ff;
  }

  .contact-page h3 {
    color: #3066be;
  }

  :global(body.dark-mode) .contact-page h3 {
    color: #9ab8ff;
  }

  .nameSplit {
    display: flex;
    flex-direction: row;
    gap: 1em;
  }

  .email {
    display: flex;
    flex-direction: row;
    align-items: center;
    margin-top: 4em;
    font-size: 1.25em;
    color: #3066be;
    padding: 0.75em 1em;
    border: 2px solid #024d98;
    border-radius: 10px;
  }

  :global(body.dark-mode) .email {
    border-color: #3066be;
    color: #9ab8ff;
  }

  @media (max-width: 1200px) {
    .section_1 {
      display: none;
    }

    .frontpage {
      justify-content: center;
      align-items: center;
    }
  }

  @media (max-width: 600px) {
    .spacer {
      height: 8em;
    }

    .nameSplit {
      flex-direction: column;
    }

    .section_2 {
      width: 100%;
      margin-left: auto;
      margin-right: auto;
    }

    .frontpage {
      padding: 0 1rem 2rem;
    }
  }
</style>