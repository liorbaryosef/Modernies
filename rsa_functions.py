import number_theory_functions as ntf


class RSA:
    def __init__(self, public_key, private_key = None):
        self.public_key = public_key
        self.private_key = private_key

    @staticmethod
    def generate(digits = 10):
        """
        Creates an RSA encryption system object

        Parameters
        ----------
        digits : The number of digits N should have

        Returns
        -------
        RSA: The RSA system containing:
        * The public key (N,e)
        * The private key (N,d)
        """
        p = ntf.generate_prime(digits)
        q = ntf.generate_prime(digits)
        N = p*q
        phi_N = (p-1)*(q-1)
        e = 1
        for i in range(2, phi_N):
            if ntf.extended_gcd(i, phi_N)[0] == 1:
                e = i
                break
        d = ntf.modular_inverse(e, phi_N)
        return RSA((N, e), (N, d))

    def encrypt(self, m):
        """
        Encrypts the plaintext m using the RSA system

        Parameters
        ----------
        m : The plaintext to encrypt

        Returns
        -------
        c : The encrypted ciphertext
        """
        N, e = self.public_key
        return ntf.modular_exponent(m, e, N)

    def decrypt(self, c):
        """
        Decrypts the ciphertext c using the RSA system

        Parameters
        ----------
        c : The ciphertext to decrypt

        Returns
        -------
        m : The decrypted plaintext
       """
        N, d = self.private_key
        return ntf.modular_exponent(c, d, N)
