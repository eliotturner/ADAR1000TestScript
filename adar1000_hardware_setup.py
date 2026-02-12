import time
from typing import List
from adi import adar1000

class ADAR1000Controller:
    ## Definition & Initial Setup
    def __init__(self, uri : str, chip_name : str):
        self.uri = uri
        self.chip_name = chip_name
        self.device = adar1000(uri=uri, 
                               chip_id=chip_name,
                               array_element_map=[[1, 2, 3, 4]],
                               channel_element_map=[1, 2, 3, 4])
        self.device.initialize(pa_off=, pa_on=, lna_off=, lna_on=)                                       ########FIX
        
        
    ##===============##
    ## Basic Control ##
    ##===============##
    
    def enable_tx(self, pa_bias : float) -> None:
        """
        Set device mode to TX, update all channels, and set PA Bias

        Parameters:
            pa_bias (float): pa_bias to be assigned (BOUNDS)
        """
        if (pa_bias >= NULL | pa_bias <= NULL)                                                         ###########FIX
            return
        self.device.mode = "tx"
        for ch in enumerate(self.device.channels):
            ch.tx_enable = True
            ch.rx_enable = False
            ch.pa_bias_on = pa_bias
        self.device.latch_tx_settings()
        
    def enable_rx(self) -> None:
        """
        Set device mode to RX, update all channels, assumes self-biased LNAs
        """
        self.device.mode = "rx"
        self.device.lna_bias_out_enable = False
        for ch in enumerate(self.device.channels):
            ch.tx_enable = False
            ch.rx_enable = True
            
        
    def disable(self) -> None:
        """
        Disable both TX and RX
        """
        self.device.mode = "disabled"
        for ch in enumerate(self.device.channels):
            ch.tx_enable = False
            ch.rx_enable = False
        
    
    ##======================##
    ## Gain & Phase Control ##
    ##======================##
    
    def set_tx_phase(self, phases : list[int]) -> None:
        """
        Set the TX phases for each channel

        Parameters:
            phases (List[int]): List of four integer phases (0-127) in order of channel
        """
        self.validate_phase_gain_vector(phases, "Phase")
        for i, ch in enumerate(self.device.channels):
            if (phases[i] >= 0 & phases[i] <= 127):
                ch.tx_phase = int(phases[i])
        self.device.latch_tx_settings()
    
    def set_tx_gain(self, gains : list[int]) -> None:
        """
        Set the TX gain for each channel

        Parameters:
            gains (List[int]): List of four integer gains (0-127) in order of channel
        """
        self.validate_phase_gain_vector(gains, "Gain")
        for i, ch in enumerate(self.device.channels):
            if (gains[i] >= 0 & gains[i] <= 127):
                ch.tx_phase = int(gains[i])
        self.device.latch_tx_settings()
        
    def set_rx_phase(self, phases : list[int]) -> None:
        """
        Set the RX phase for each channel

        Parameters:
            phases (List[int]): List of four integer phases (0-127) in order of channel
        """
        self.validate_phase_gain_vector(phases, "Phases")
        for i, ch in enumerate(self.device.channels):
            if (phases[i] >= 0 & phases[i] <= 127):
                ch.rx_phase = int(phases[i])
        self.device.latch_rx_settings()
    
    def set_rx_gain(self, gains : list[int]) -> None:
        """
        Set the RX gain for each channel

        Parameters:
            gains (List[int]): List of four integer gains (0-127) in order of channel
        """
        self.validate_phase_gain_vector(gains, "Gain")
        for i, ch in enumerate(self.device.channels):
            ch.rx_phase = int(gains[i])
        self.device.latch_rx_settings()


    ##=======================##
    ## TX Exclusive Controls ##
    ##=======================##

    def set_pa_bias(self, bias : float) -> None:
        """
        Set the phases for a single ADAR1000

        Parameters:
            bias (float): The PA-bias to be set
        """
        for i, ch in enumerate(self.device.channels):
            if (bias >= -5 & bias <= 5):                                            ## ADD REASONABLE BOUNDS IDK
                ch.pa_bias_on = bias
        self.device.latch_tx_settings()
    
    
    ##============##
    ## Monitoring ##
    ##============##
    
    def read_temperature(self):
        """
        Reads on-chip temperature sensor
        """
        temp = self.device.temperature
        return temp
    
    
    ##==================##
    ## Helper Functions ##
    ##==================##
    
    def validate_phase_gain_vector(self, vec : List[int], name : str):
        if not isinstance(vec, List) or len(vec) != 4:
            raise ValueError(f"{name} must be provided as a list of 4 integers")
        for val in vec:
            if not isinstance(val, int):
                raise ValueError(f"{name} entries must be integers")
            if not 0 <= val <= 127:
                raise ValueError(f"{name} values must be between 0 and 127")




adar = ADAR1000Controller(uri=, chip_name='BEAM_TX')

"""
for i in range(100):
    print(f"Temp #{i}: {adar.read_temperature()}")
    time.sleep(1)
"""

# adar.set_tx_gain([127, 127, 127, 127])