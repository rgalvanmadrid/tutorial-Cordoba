import matplotlib.pyplot as plt
import matplotlib.colors as colors

def twoband_maps(data_lowfreq, data_highfreq, noise_lowfreq=0.1e-3, 
                 noise_highfreq=0.1e-3, thr_lowfreq=1,  thr_highfreq=1,
                 title_lowfreq='Low frequency map', 
                 title_highfreq='High frequency map',
                 ticks_lowfreq=[-1e-3,1e-3,1e-2,1e-1], 
                 ticks_highfreq=[-1e-3,1e-3,1e-2,1e-1],
                 squeeze=True,
                 **kwargs):
    if squeeze==True:
        data_lowfreq = data_lowfreq.squeeze()
        data_highfreq = data_highfreq.squeeze()

    fig = plt.figure(figsize=(9, 5))
    ax1 = plt.subplot(1, 2, 1)
    ax2 = plt.subplot(1, 2, 2)

    norm1 = colors.SymLogNorm(linthresh=thr_lowfreq*noise_lowfreq,linscale=0.1, 
                              base=10)
    im1 = ax1.imshow(data_lowfreq, origin='lower', cmap='Oranges', norm=norm1)
    ax1.set_title(title_lowfreq)
    cbar1 = plt.colorbar(im1, ax=[ax1], shrink=0.7, pad=0.02, ticks=ticks_lowfreq)

    norm2 = colors.SymLogNorm(linthresh=thr_highfreq*noise_highfreq,linscale=0.1, 
                              base=10)
    im2 = ax2.imshow(data_highfreq, origin='lower', cmap='Oranges', norm=norm2)
    ax2.set_title(title_highfreq)
    cbar2 = plt.colorbar(im2, ax=[ax2], shrink=0.7, pad=0.02, ticks=ticks_highfreq)
    return fig

    