# -*- coding: utf-8 -*-

"""
    healthoslib.models.common_side_effects_response
 
    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ) on 02/18/2017
"""
import healthoslib.models.side_effect
import healthoslib.models.base_model

class CommonSideEffectsResponse(healthoslib.models.base_model.BaseModel):

    """Implementation of the 'Common Side EffectsResponse' model.

    TODO: type model description here.

    Attributes:
        generic (string): TODO: type description here.
        side_effects (list of SideEffect): TODO: type description here.

    """

    def __init__(self, 
                 generic = None,
                 side_effects = None):
        """Constructor for the CommonSideEffectsResponse class"""
        
        # Initialize members of the class
        self.generic = generic
        self.side_effects = side_effects

        # Create a mapping from Model property names to API property names
        self.names = {
            "generic" : "generic",
            "side_effects" : "side_effects",
        }


    @classmethod
    def from_dictionary(cls, 
                        dictionary):
        """Creates an instance of this model from a dictionary
       
        Args:
            dictionary (dictionary): A dictionary representation of the object as
            obtained from the deserialization of the server's response. The keys
            MUST match property names in the API description.
            
        Returns:
            object: An instance of this structure class.
            
        """
        if dictionary == None:
            return None
        else:
            # Extract variables from the dictionary
            generic = dictionary.get("generic")
            side_effects = None
            if dictionary.get("side_effects") != None:
                side_effects = list()
                for structure in dictionary.get("side_effects"):
                    side_effects.append(healthoslib.models.side_effect.SideEffect.from_dictionary(structure))
            # Return an object of this model
            return cls(generic,
                       side_effects)

