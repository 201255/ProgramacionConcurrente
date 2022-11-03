# empty (m_x):
# 2 if m_x_count == 0:
# 3 return (True)
# 4 else:
# 5 return (False)
# 6
# 7 resume(m_x):
# 8 if m_x_count != 0:
# 9 m_next_count = m_next_count + 1
# 10
# 11 signal(m_x_sem) # Libera al siguiente proceso en la cola de la
# 12 wait(m_next) # variable de condición y se bloquea en la cola
# 13 # de cortesía
# 14
# 15 m_next_count = m_next_count - 1
# 16
# 12
# 17 delay(m_x):
# 18 m_x_count = m_x_count + 1
# 19
# 20 # Alguien puede ocupar el monitor: puede ser de la cola de cortesía
# 21 # primero o de la entrada normal al monitor
# 22 if m_next_count != 0:
# 23 signal(m_next)
# 24 # Libera al siguiente proceso: tienen
# 25 # preferencia los de la cola de cortesía
# 26 else:
# 27 signal(m_mutex)
# 28
# 29 wait(m_x_sem) # Se bloquea en la variable de condición m_x
# 30 m_x_count = m_x_count - 1