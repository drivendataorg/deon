# Test interaktywny z filozofii

Samodzielny (jednoplikowy) test wiedzy w HTML — **30 pytań jednokrotnego wyboru**
z podstawowych kategorii filozoficznych, obejmujących całą historię filozofii:
od presokratyków, przez starożytność, średniowiecze i nowożytność, po filozofię
współczesną.

## Uruchomienie

Otwórz `index.html` w dowolnej przeglądarce — nie wymaga instalacji, serwera ani
połączenia z internetem (cały kod HTML/CSS/JS jest w jednym pliku).

## Zakres tematyczny

Pytania pokrywają główne działy filozofii:

- **Metafizyka / ontologia** (arché, byt, idee, substancja, dialektyka)
- **Epistemologia** (racjonalizm, empiryzm, sceptycyzm, pragmatyzm, Kant)
- **Etyka** (cnota, stoicyzm, epikureizm, imperatyw kategoryczny, utylitaryzm, egzystencjalizm)
- **Logika i filozofia nauki** (sylogizm, falsyfikacja)
- **Filozofia polityczna** (Hobbes, Rousseau, Marks)
- **Filozofia religii** (Augustyn, Tomasz z Akwinu)
- **Filozofia umysłu i języka** (fenomenologia, Wittgenstein)
- **Estetyka**

## Funkcje

- Natychmiastowe wyjaśnienie po wyborze każdej odpowiedzi
- Pasek postępu
- Podsumowanie wyniku z rozbiciem na kategorie
- Tryb jasny i ciemny (dopasowuje się do ustawień systemu)
- Możliwość rozwiązania testu ponownie
- Wysyłka wyniku na e-mail przez [Web3Forms](https://web3forms.com)

## Konfiguracja wysyłki wyniku (Web3Forms)

Po zakończeniu testu uczestnik może wysłać swój wynik na e-mail właściciela
formularza. Wykorzystujemy do tego usługę Web3Forms (bez własnego backendu).

Aby to działało, wystarczy jeden klucz dostępu:

1. Wejdź na https://web3forms.com i wygeneruj **Access Key** (podając e-mail,
   na który mają przychodzić wyniki).
2. W pliku `index.html` znajdź na początku sekcji `<script>` linię:

   ```js
   const WEB3FORMS_ACCESS_KEY = "TWOJ_KLUCZ_TUTAJ";
   ```

3. Wklej swój klucz między cudzysłowy.

Klucz Web3Forms jest **publiczny** i z założenia umieszcza się go w kodzie
front-endu — nie jest to sekret. Wyniki (imię, opcjonalny e-mail, punktacja
oraz rozbicie na kategorie) trafiają na adres przypisany do klucza.

Test ma charakter edukacyjny.
