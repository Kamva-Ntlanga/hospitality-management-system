from enum import Enum
from datetime import datetime

class PaymentStatus(Enum):
    PENDING = "Pending"
    AUTHORIZED = "Authorized"
    CAPTURED = "Captured"
    FAILED = "Failed"
    REFUNDED = "Refunded"

class PaymentMethod(Enum):
    CREDIT_CARD = "Credit Card"
    CASH = "Cash"
    DIGITAL_WALLET = "Digital Wallet"

class Payment:
    def __init__(self, payment_id: str, amount: float, method: PaymentMethod, booking):
        self._payment_id = payment_id
        self._amount = amount
        self._method = method
        self._booking = booking
        self._payment_date = None
        self._status = PaymentStatus.PENDING
        self._transaction_id = ""

    def get_payment_id(self) -> str:
        return self._payment_id

    def get_amount(self) -> float:
        return self._amount

    def get_method(self) -> PaymentMethod:
        return self._method

    def get_status(self) -> PaymentStatus:
        return self._status

    def get_transaction_id(self) -> str:
        return self._transaction_id

    def authorize(self) -> bool:
        if self._amount > 0:
            self._status = PaymentStatus.AUTHORIZED
            self._payment_date = datetime.now()
            self._transaction_id = f"TXN_{self._payment_id}_{int(datetime.now().timestamp())}"
            return True
        self._status = PaymentStatus.FAILED
        return False

    def capture(self) -> bool:
        if self._status == PaymentStatus.AUTHORIZED:
            self._status = PaymentStatus.CAPTURED
            return True
        return False

    def refund(self) -> bool:
        if self._status == PaymentStatus.CAPTURED:
            self._status = PaymentStatus.REFUNDED
            return True
        return False

    def generate_receipt(self) -> str:
        receipt = f"""
        RECEIPT
        =======
        Payment ID: {self._payment_id}
        Date: {self._payment_date}
        Amount: ${self._amount:.2f}
        Method: {self._method.value}
        Transaction ID: {self._transaction_id}
        Status: {self._status.value}
        """
        return receipt

    def __str__(self) -> str:
        return f"Payment {self._payment_id}: ${self._amount} - {self._status.value}"
