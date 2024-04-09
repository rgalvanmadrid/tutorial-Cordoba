import numpy as np

from astropy.io import fits
from astropy.convolution import convolve, convolve_fft
from astropy import wcs

from radio_beam import Beam
from reproject import reproject_interp

def convol(input_im,template_im,**kwargs):
    # Read in images and headers
    fh1 = fits.open(input_im)
    header1 = fits.getheader(input_im)
    beam1 = Beam.from_fits_header(header1)
    print(beam1)
    fh2 = fits.open(template_im)
    header2 = fits.getheader(template_im)
    beam2 = Beam.from_fits_header(header2)
    print(beam2)
    # Find and create convolution kernel
    try:
        conv_beam = beam2.deconvolve(beam1)
        print(conv_beam)
        pix_scale = header1['CDELT2']*u.deg
        pix_scale = pix_scale.to(u.arcsec)
        conv_beam_kernel = conv_beam.as_kernel(pix_scale)
        # Convolve in Fourier space. Need to scale to Jy/pix before
        abeam1 = 1.442*(np.pi/4)*header1['BMAJ']*header1['BMIN']*3600**2
        abeam2 = 1.442*(np.pi/4)*header2['BMAJ']*header2['BMIN']*3600**2
        apix  = (header1['CDELT2']*3600)**2
        convldata = np.copy(fh1[0].data)
        convldata[0,0,:,:]=(abeam2/apix)*convolve_fft((apix/abeam1)
        *fh1[0].data[0,0,:,:],conv_beam_kernel,preserve_nan=True)
        #convldata = np.where(np.abs(convldata) < 1e-5, np.nan, convldata)
    except:
         convldata = np.copy(fh1[0].data)
    # Update header and save to fits
    del header1['HISTORY']
    header1['BMAJ'] = header2['BMAJ']
    header1['BMIN'] = header2['BMIN']
    header1['BPA'] = header2['BPA']
    conv_image = input_im.replace('.fits','.conv.fits')
    fits.writeto(conv_image,convldata,header1,overwrite=True)
    fh1.close()
    fh2.close()
    print('Created '+conv_image)
    return conv_image


def regrid(input_im,template_im,**kwargs):
    fh1 = fits.open(input_im)
    fh2 = fits.open(template_im)
    w1 = wcs.WCS(fh1[0].header)
    w2 = wcs.WCS(fh2[0].header)
    repr,_ = reproject_interp((fh1[0].data, w1.celestial), w2.celestial, shape_out=fh2[0].data.squeeze().shape)
    outhead = w2.celestial.to_header()
    outhead['BMAJ'] = fh1[0].header['BMAJ']
    outhead['BMIN'] = fh1[0].header['BMIN']
    outhead['BPA'] = fh1[0].header['BPA']
    outhead['BTYPE'] = fh1[0].header['BTYPE']
    outhead['OBJECT'] = fh1[0].header['OBJECT']
    outhead['BUNIT'] = fh1[0].header['BUNIT']
    hdu = fits.PrimaryHDU(data=repr, header=outhead)
    regr_image = input_im.replace('.fits','.regr.fits')
    hdu.writeto(regr_image,overwrite=True)
    fh1.close()
    fh2.close()
    print('Created '+regr_image)
    return regr_image