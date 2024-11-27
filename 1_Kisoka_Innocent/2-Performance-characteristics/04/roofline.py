import matplotlib.pyplot as plt
import numpy as np

def plot_roofline(Pmax, bmax, Imin, Imax, N=1000, ax=None, **plt_kwargs):
    """
    
    Parameters:
    - Pmax: Peak performance (in GFLOPS/s).
    - bmax: Maximum memory bandwidth (in GB/s).
    - Imin: Minimum operational intensity.
    - Imax: Maximum operational intensity.
    - N: Number of points for plotting.
    - ax: Axes to plot on (optional).
    - plt_kwargs: Additional plot arguments.
    """
    if ax is None:
        ax = plt.gca()
    
    #Generate operational intensity values on a logarithmic scale
    I = np.logspace(np.log10(Imin), np.log10(Imax), N)
    
    # Compute performance: Memory bandwidth-limited and compute-limited
    P = bmax * I
    P = np.minimum(P, Pmax)  # Limit by peak performance
    
    # Plot the roofline curve
    ax.loglog(I, P, **plt_kwargs)
    
    # Set the scale and labels
    ax.set_xscale('log', base=2)
    ax.grid(True)
    ax.set_xlim(Imin, Imax)
    ax.set_xlabel(rf"Operational Intensity $I$ [Flops/Byte]")
    ax.set_ylabel(rf"Performance $P$ [GFLOPs/s]")
    return ax

if __name__ == "__main__":
    # Constants
    peak_performance = 36.8  # Peak performance in GFLOPs/s
    memory_bandwidth = 19.199  # Memory bandwidth in GB/s (converted from MB/s)
    Imin = 1.e-2  # Minimum operational intensity
    Imax = 1.e+2  # Maximum operational intensity

    # Performance data for different operations
    operations = ['Copy', 'Scale', 'Add', 'Triad']
    performance_rates = [19199.6, 11241.7, 12298.3, 12302.5]  # Performance rates in MB/s
    operational_intensity = [0.25, 0.25, 0.25, 0.375]  # Flops/Byte

    # Convert performance rates to GFLOPs/s
    performance_rates_gflops = [rate / 1000 for rate in performance_rates]

    # Create the plot
    fig, ax = plt.subplots()
    
    # Plot the roofline
    ax = plot_roofline(Pmax=peak_performance, bmax=memory_bandwidth, Imin=Imin, Imax=Imax, ax=ax, label="Roofline")

    # Plot the performance points
    for i, op in enumerate(operations):
        ax.scatter(operational_intensity[i], performance_rates_gflops[i], label=f'{op} Performance', s=100)

    
    ridge_point = 36.8/19.199  
    ax.axvline(x=ridge_point, color='gray', linestyle='--', label=f'Ridge Point (Iridge ≈ {ridge_point})')

    # Final plot adjustments
    ax.legend()
    plt.grid(True, which="both", ls="--")
    plt.title('Roofline Model for Rosa Node')
    
    # Show plot
    plt.show()
