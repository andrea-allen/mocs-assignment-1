
#These methods contain the simplest implementation of Euler and Heun Methods
#For use cases, see SIS_deterministic
def euler_step(h, x_t, dx_dt):
    x_t_plus_h = x_t + h*dx_dt
    return x_t_plus_h

def heun_step(h, x_t, dx_dt, dx_dt_eu):
    x_t_plus_h_hn = x_t + (h/2)*(dx_dt + dx_dt_eu)
    return x_t_plus_h_hn