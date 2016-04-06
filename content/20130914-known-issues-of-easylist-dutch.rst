Known issues of EasyList Dutch
##############################

:date: 2013-09-14 18:40
:tags: known issues, EasyList Dutch
:category: Articles
:slug: 2013/09/14/known-issues-of-easylist-dutch
:authors: Famlam

This post lists the known issues of EasyList Dutch (previously DutchAdblockList), in Dutch.

**De volgende problemen op Nederlandstalige websites zijn bekend**:

------------

**Probleem**
  Het is niet mogelijk om spoilers te openen op het forum van fok.nl

**Betrokken domein**
  - forum.fok.nl

**Oplossing**
  U kunt dit oplossen door advertenties toe te staan op deze pagina's door het volgende filter toe te voegen: ``@@||forum.fok.nl/topic/$document``

------------

**Probleem**
  Spellen op spelletjes.nl en spel.nl starten vertraagd

**Betrokken domeinen**
  - spelletjes.nl
  - spel.nl

**Details**
  Op deze websites voor spelletjes starten de spellen pas na enkele tientallen seconden. Dit komt omdat de website op de achtergrond denkt dat er een advertentie gedurende die tijd bezig is, en het spel pas start als die tijd over is. De advertentie is natuurlijk geblokkeerd, maar de tijd kan niet overgeslagen worden.

**Oplossing**
  Geen. Wacht tot het spel vanzelf start

------------

**Probleem**
  Sommige advertenties in videos en games kunnen niet geblokkeerd worden

**Details**
  In videos/games van enkele domeinen kunnen videoadvertenties niet geblokkeerd worden omdat de video/game dan zelf niet meer af kan spelen

**Betrokken domeinen**
  - 538.nl
  - herhaling.nl
  - kinderspelletjes.nl
  - ongein.nl
  - radio10.nl
  - radioluisteren.fm
  - radioveronica.nl
  - rtl7darts.nl
  - skyradio.nl
  - tvgids.tv
  - twentefans.nl
  - vmma.be
  - voetbalprimeur.nl
  - vtm.be

**Oplossing**
  Geen. Wacht tot de advertentie afgelopen is

------------

**Probleem**
  Een lege popup verschijnt op tvgids.nl

**Details**
  Op tvgids.nl zal bij het laden van de pagina een lege popup verschijnen, waarin oorspronkelijk advertenties stonden. Deze kan niet in de lijst geblokkeerd worden, omdat dan ook enkele legitieme onderdelen van de site niet meer functioneren. 

**Betrokken domein**
  - tvgids.nl

**Oplossing**
  Wilt u de popup toch blokkeren, voeg dan zelf het volgende filter toe: ``tvgids.nl###simplemodal-container,#simplemodal-overlay``

------------

**Probleem**
  De melding *"Ad block gedetecteerd, de mogelijkheid tot het afspelen van de video wordt uitgeschakeld"*

**Details**
  Op enkele domeinen wordt *in FireFox* de melding getoond dat er een adblocker gedetecteerd is. Helaas detecteren deze websites niet of Adblock Plus actief is, maar alleen of het geïnstalleerd is. Daardoor helpt ook het uitschakelen van ABP op deze websites niet.

**Betrokken domeinen**
  - kijk.nl
  - nu.nl (de sportvideos)

**Oplossing**
  Dit probleem vindt alleen in FireFox plaats. U kunt de videos in een andere browser bekijken.

------------

Andere problemen gevonden op Nederlandstalige websites? Geef dit dan door in het `forum`_ van EasyList Dutch of stuur een email naar het adres in de `filterlijst`_.

.. _`forum`: https://forums.lanik.us/viewforum.php?f=100
.. _`filterlijst`: https://easylist-downloads.adblockplus.org/easylistdutch.txt