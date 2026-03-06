from .client import VaultClient
import hvac.exceptions

def get_vault_secret(mount_point, path, key):
    try:
        client = VaultClient().get_client()
        secret = client.secrets.kv.v2.read_secret_version(
            mount_point=mount_point,
            path=path,
            raise_on_deleted_version=True
        )
        return secret['data']['data'].get(key)
    except hvac.exceptions.VaultError as e:
        print(f"Vault error: {e}")
    except Exception as e:
        print(f"Error: {e}")
    return None

