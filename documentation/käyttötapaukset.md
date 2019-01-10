# Heppa käyttötapaukset

Lihavoidut on toteutettu

* **Käyttäjä voi nähdä listan ehdokkaista**
    * **Käyttäjä voi nähdä montako ääntä** (ja vetoa) **ehdokkaat ovat saaneet**
    * Käyttäjä voi nähdä listan entisistä eli valituista ehdokkaista
        * Käyttäjä voi nähdä milloin ehdokas valittiin
    * **Käyttäjä voi nähdä mikä ehdokas voittaa sen hetkisillä äänillä**
    * Käyttäjä voi nähdä kaikki annetut äänet
        * Käyttäjä voi merkitä joidenkin käyttäjätilien äänet ohitettaviksi hänelle näkyvissä laskuissa
* **Rekisteröimätön käyttäjä voi luoda käyttäjätilin voidakseen kirjautua sisään**
    * **Rekisteröitynyt käyttäjä voi kirjautua sisään voidakseen äänestää**
        * **Sisään kirjautunut käyttäjä voi lisätä ehdokkaan**
        * Sisään kirjautunut käyttäjä voi muokata lisäämäänsä ehdokkaan tietoja
            * Ehdokkalle voi lisätä tageja
        * Sisään kirjautunut käyttäjä voi poistaa lisäämänsä ehdokkaan
        * **Sisään kirjautunut käyttäjä voi merkitä hyväksyvänsä ehdokkaan**
        * Sisään kirjautunut käyttäjä voi merkitä vetovansa ehdokkaan
        * **Sisään kirjautunut käyttäjä voi merkitä lisäämänsä ehdokkaan valituksi**

## Avoimia kysymyksiä

* Miten otetaan huomioon se, että ehdottaja ei välttämättä ole paikalla?
    * Voisi tehdä niin, että ehdotukset tallentuvat mutta ne pitää uudelleenaktivoida joka viikko. Tämä vaatisi siis että ehdokkailla on "aktiivinen" kenttä. Epä-aktiivisia ehdokkaita ei siis tulisi näkyä listalla, tai ainakaan niitä ei pitäisi voida äänestää.