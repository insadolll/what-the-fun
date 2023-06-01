from django_auth_ldap.forms import LDAPAuthenticationForm

class CustomLDAPAuthenticationForm(LDAPAuthenticationForm):
    """Override the default LDAPAuthenticationForm to customize the login form"""
    # Add any customizations to the login form here