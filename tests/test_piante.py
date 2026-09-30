from app.classi import Agrume, Pomodoro, Basilico, Aloe


def test_annaffia():
    pianta = Agrume("limone", 20)

    pianta.giorni_senza_acqua = 10

    pianta.annaffia()

    assert pianta.giorni_senza_acqua == 0


def test_bisogna_annaffiare():
    pianta = Agrume("limone", 20)

    pianta.giorni_senza_acqua = 7

    assert pianta.bisogna_annaffiare() is True


def test_non_bisogna_annaffiare():
    pianta = Agrume("limone", 20)

    pianta.giorni_senza_acqua = 3

    assert pianta.bisogna_annaffiare() is False


def test_cresce():
    pianta = Pomodoro("ciliegino", 20)

    altezza_iniziale = pianta.altezza

    pianta.cresce()

    assert pianta.altezza > altezza_iniziale


def test_cogli_frutti():
    pianta = Agrume(
        "limone",
        20,
        num_frutti=10
    )

    pianta.cogli(3)

    assert pianta.num_frutti == 7


def test_cogli_troppi_frutti():
    pianta = Agrume(
        "limone",
        20,
        num_frutti=2
    )

    try:
        pianta.cogli(5)
        assert False
    except ValueError:
        assert True


def test_travaso():
    pianta = Agrume("limone", 10)

    pianta.altezza = 250

    assert pianta.bisogna_travasare() is True


def test_basilico_foglie():
    pianta = Basilico("basilico", 20)
    foglie_iniziali = pianta.num_foglie

    pianta.giorni_senza_acqua = 1

    pianta.cresce_foglie()

    assert pianta.num_foglie == foglie_iniziali + 1


def test_pomodoro_frutti():
    pianta = Pomodoro("pomodoro", 20)

    frutti_iniziali = pianta.num_frutti

    pianta.giorni_senza_acqua = 1

    pianta.cresce_frutti()

    assert pianta.num_frutti > frutti_iniziali


def test_aloe_raccolta():
    aloe = Aloe("aloe", 30)

    risultato = aloe.cogli(3)

    assert "Gel di aloe" in risultato