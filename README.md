\# Lorentz-muunnoksen animaatio



Interaktiivinen visualisointi erityisen suhteellisuusteorian Lorentz-muunnoksesta Minkowskin diagrammin avulla.



\## Mitä animaatio näyttää



Animaatiossa on kaksi rinnakkaista kuvaajaa:



1\. \*\*Lepojärjestelmä S\*\* – Kiinteät x- ja ct-akselit. Näyttää kuinka liikkuvan järjestelmän S' akselit (x' ja ct') kallistuvat suhteessa lepojärjestelmään, kun nopeus β = v/c muuttuu väliltä -0.9c ... 0.9c.



2\. \*\*Liikkuva järjestelmä S'\*\* – Näyttää saman tapahtuman E koordinaatit (x', ct') liikkuvan havaitsijan näkökulmasta. Pisteen rata piirtää hyperbelin, koska Lorentz-muunnos säilyttää invariantin suureen x'² - ct'² vakiona kaikilla nopeuksilla.



\## Fysikaalinen tausta



\- Tapahtuma E on kiinnitetty pisteeseen (x=2, ct=3) lepojärjestelmässä.

\- Lorentz-muunnos: x' = γ(x - βct), ct' = γ(ct - βx), missä γ = 1/√(1-β²).

\- Valokartion viivat (ct = ±x) on piirretty molempiin kuvaajiin invarianttina referenssinä.

\- x'- ja ct'-akselit lasketaan asettamalla vastaavasti ct'=0 ja x'=0, mikä antaa kaavat ct=βx ja ct=x/β.



\## Käyttö



Vaatii Python-kirjastot `matplotlib` ja `numpy`:

Animaatio pyyhkäisee nopeuden β edestakaisin väliltä -0.9c...0.9c ja takaisin, toistuen loputtomasti.

