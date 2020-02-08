import datetime as dt

MSG_STARTTIME = "Выполнение началось в: {0}"
MSG_STOPTIME = "Выполнение закончилось в: {0}"
MSG_EXECTIME = "Длительность выполнения: {0}"


class Counter:
    def __enter__(self):
        self._start_time = dt.datetime.now()

    def __exit__(self, exc_type, exc_val, ext_tb):
        stop_time = dt.datetime.now()
        exec_time = stop_time - self._start_time
        print(MSG_STARTTIME.format(self._start_time))
        print(MSG_STOPTIME.format(stop_time))
        print(MSG_EXECTIME.format(exec_time))
