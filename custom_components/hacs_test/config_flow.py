"""Config flow for HACS Test integration."""

from homeassistant import config_entries

DOMAIN = "hacs_test"


class HacsTestConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for HACS Test."""

    VERSION = 1

    async def async_step_user(self, user_input=None):
        """Handle the initial step."""
        if user_input is not None:
            return self.async_create_entry(title="HACS Test", data={})

        return self.async_show_form(step_id="user")
