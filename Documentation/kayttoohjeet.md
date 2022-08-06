# Käyttöohjeet

Ohjelma kääntää logo-kielellä kirjoitetun tiedoston leJOS NXJ-käyttöjärjestelmän tukemaksi java-tiedostoksi. leJOS tarvitsee oman versionsa java-kääntäjästä. Tarkemmat ohjeet kääntäjän asentamiseen löytyvät [täältä](https://lejos.sourceforge.io/).

## Logo-tiedosto

Tiedoston tulee olla nimetty päätteellä ```.logo```. 

### Merkkijonot ja muuttujat
Logossa merkkijono tunnistetaan jonoa edeltävällä lainausmerkillä, esim. käsky ```tulosta "merkkijono``` tulostaa
> merkkijono


Toisaalta muuttujan asettava käsky *olkoon* vaatii muuttujan eteen myös lainausmerkit. Muuttujaa kutsutaan asettamalla sen eteen kaksoispiste.
~~~~
olkoon "jono "merkkijono
show :jono
~~~~
> merkkijono
>


Numeroille ei luonnollisesti tarvitse lainausmerkkejä:
~~~~
olkoon "iq 120
show :iq
~~~~
> 120

### Laskujärjestys

Funktioiden osalta laskujärjestys tulee huomioida. **Koska funktioiden parametria ei tarvitse laittaaa sulkeiden sisään, ei laskujärjestys aina ole intuitiivinen.** Muilta osin Logo noudattaa aritmetiikan laskusääntöjä

Esim. ```SQRT 4 + 4 / 2``` on Logossa sama kuin ```SQRT (4 + 4 / 2)``` eli ```SQRT (4 + 2)``` eli ```SQRT 6```

## Tuetut komennot

### Liikuttaminen

| Komento       |  Tehtävä                               | Parametri                                                          |
|:-------------:|:--------------------------------------:|:------------------------------------------------------------------:|
|  Eteen        |  Liikuttaa robottia eteenpäin          | Numero tai numeron palauttava funktio tai laskutoimitus            |
|  Taakse       |  Liikuttaa robottia taaksepäin         | Sama kuin yllä                                                     |
|  Vasemmalle   |  Kääntää robottia vasemmalle           | Sama kuin yllä                                                     |
|  Oikealle     |  Kääntää robottia oikealle             | Sama kuin yllä                                                     |
|  Tulosta      |  Tulostaa robotin ruudulle             | Numero, laskutoimitus, merkkijono tai sellaisen palauttava funktio |


### Matemaattiset operaatiot

| Nimi                   | Funktio tai symboli | Tehtävä                                                       |
|------------------------|---------------------|---------------------------------------------------------------|
| Peruslaskutoimitukset  | + - * /             | Perusaritmetiikka                                             |
| Neliöjuuri             | SQRT                | Palauttaa neliöjuuren annetusta luvusta                       |



## Kääntäjän käyttäminen

Kääntäjä suoritetaan Linuxilla komentoriviltä. Pääohjelma compile.py suoritetaan **ohjelman juurihakemistosta** käskyllä

```python3 compile.py [logo-ohjelman nimi ja tarvittaessa hakemisto jos se ei ole juurihakemistossa]```

Käännetty Java-ohjelma on juurihakemistossa oleva Main.java.


