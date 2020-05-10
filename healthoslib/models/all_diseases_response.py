# -*- coding: utf-8 -*-

"""
    healthoslib.models.all_diseases_response
 
    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ) on 02/18/2017
"""
import healthoslib.models.base_model

class AllDiseasesResponse(healthoslib.models.base_model.BaseModel):

    """Implementation of the 'All DiseasesResponse' model.

    TODO: type model description here.

    Attributes:
        disease_name (string): TODO: type description here.
        disease_cat (string): TODO: type description here.
        disease_info (string): TODO: type description here.
        disease_id (string): TODO: type description here.

    """

    def __init__(self, 
                 disease_name = None,
                 disease_cat = None,
                 disease_info = None,
                 disease_id = None):
        """Constructor for the AllDiseasesResponse class"""
        
        # Initialize members of the class
        self.disease_name = disease_name
        self.disease_cat = disease_cat
        self.disease_info = disease_info
        self.disease_id = disease_id

        # Create a mapping from Model property names to API property names
        self.names = {
            "disease_name" : "disease_name",
            "disease_cat" : "disease_cat",
            "disease_info" : "disease_info",
            "disease_id" : "disease_id",
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
            disease_name = dictionary.get("disease_name")
            disease_cat = dictionary.get("disease_cat")
            disease_info = dictionary.get("disease_info")
            disease_id = dictionary.get("disease_id")
            # Return an object of this model
            return cls(disease_name,
                       disease_cat,
                       disease_info,
                       disease_id)

