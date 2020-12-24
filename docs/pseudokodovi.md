# Upis

ispisiObrazac:
    if greske:
        print(obrazac.greske)
        print(obrazac)
        obrazac.ispuni()
        validirajObrazac(obrazac)
    
    else:
        print(obrazac)
        obrazac.ispuni()
        validirajObrazac(obrazac)


validirajObrazac:
    if obrazac.podaci_validirani:
        obrazac.spremi()
        odobriObrazac()
    else:
        greske = "Greška"
        ispisiObrazac()

odobriObrazac:
    if prijavljeni_korisnik == administrator:
        obrazac.odobren.ispuni()
        obrazac.obrazlozenje.ispuni()

        podaci_roditelj = obrazac.podaci.roditelj
        podaci_dijete = obrazac.podaci.dijete

        if obrazac.odobren:
            roditelj = Roditelj(podaci_roditelj)
            if not roditelj.postoji:
                roditelj = Roditelj(podaci_roditelj).spremi()
            Dijete(podaci_dijete).spremi()
            roditelj.obavijesti_email()
        else:
            obavijesti_email(podaci_roditelj)
    else:
        print(obrazac.spremljen)


obrazac = Obrazac()
ispisiObrazac()


# Autentikacija

autentikacijaObrazac:
    if greske:
        print(obrazac.greske)
        print(obrazac)
        obrazac.ispuni()
        validirajObrazac(obrazac)
    
    else:
        print(obrazac)
        obrazac.ispuni()
        validirajObrazac(obrazac)
    

validirajObrazac:
    if obrazac.podaci_validirani:
        obrazac.spremi()
        prijaviKorisnika()
    else:
        greske = "Greška"
        autentikacijaObrazac()

prijaviKorisnika:
    email = obrazac.email
    lozinka = obrazac.lozinka

    korisnik = Korisnik(email)

    if korisnik:
        if korisnik.lozinka == lozinka:
            prijavljeni_korisnik = korisnik

            if prijavljeni_korisnik == roditelj:
                print(stranica_roditelj)
            else if prijavljeni_korisnik == djelatnik:
                print(stranica_djelatnik)
            else if prijavljeni_korisnik == administrator:
                print(stranica_administrator)
            else:
                greska = "Vaša uloga nije definirana. Obratite se administratoru"
                autentikacijaObrazac()
        else:
            greska = "Unesena lozinka nije točna"
            autentikacijaObrazac()
    else:
        greska = "Korisnik s emailom ne postoji"
        autentikacijaObrazac()


obrazac = AutentikacijaObrazac()
autentikacijaObrazac()