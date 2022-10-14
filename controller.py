import find
import inp
import logg
import salary
import add
import dlt

def work_with_phonk():
    a = inp.show_menu()

    if a == 1:
        name = inp.last_name()
        find.PersonFinder(name)
        logg.log_info(name)
    elif a == 2:
        job = inp.PostJob()
        find.PersonFinder(job)
        logg.log_info(job)
    elif a == 3:
        zarplata = inp.zp()
        salary.SalWal(zarplata)
        logg.log_info(zarplata)
    elif a == 4:
        person = inp.AddPer()
        add.impo(person)
        logg.log_info(person)
    elif a ==  5:
        choz = inp.DelPerson()
        dlt.delit(choz)
        logg.log_info(str(choz))
    elif a == 6:
        ...