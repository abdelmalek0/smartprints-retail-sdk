from datetime import datetime
from typing import Any
from typing import Dict
from typing import Optional

from pydantic import Field
from smartprints_core.models import SmartprintsBaseModel


class Client(SmartprintsBaseModel):
    created_date: Optional[datetime] = Field(None, alias="createdDate")
    modified_date: Optional[datetime] = Field(None, alias="modifiedDate")
    created_by: Optional[str] = Field(None, alias="createdBy")
    modified_by: Optional[str] = Field(None, alias="modifiedBy")
    id: Optional[int] = Field(None, alias="idCLIENT")
    address: Optional[str] = None
    city: Optional[str] = None
    contact: Optional[str] = None
    contact_phone: Optional[str] = Field(None, alias="contactPhone")
    description: Optional[str] = None
    email: Optional[str] = None
    fax: Optional[str] = None
    mobile: Optional[str] = None
    name: Optional[str] = None
    name_ar: Optional[str] = None
    phone: Optional[str] = None
    site: Optional[str] = None
    status: Optional[str] = None
    vat: Optional[Any] = None  # Using Any to handle both string and float
    has_integration: Optional[bool] = Field(None, alias="hasIntegration")
    integration_type: Optional[str] = Field(None, alias="integrationType")
    crn_number: Optional[str] = Field(None, alias="crnNumber")
    street: Optional[str] = None
    building_number: Optional[str] = Field(None, alias="buildingNumber")
    plot_identification: Optional[str] = Field(None, alias="plotIdentification")
    city_subdivision_name: Optional[str] = Field(None, alias="citySubdivisionName")
    city_name: Optional[str] = Field(None, alias="cityName")
    postal_zone: Optional[str] = Field(None, alias="postalZone")
    party_legal_entity_registration_name: Optional[str] = Field(None, alias="partyLegalEntityRegistrationName")
    activate_zatca: Optional[bool] = Field(None, alias="activateZatca")
    links: Optional[Dict[str, Any]] = Field(None, alias="_links")
