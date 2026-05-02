from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount: float) -> bool:
        pass
    @abstractmethod
    def get_processor_name(self) -> str:
        pass

class CreditCardProcessor(PaymentProcessor):
    def process_payment(self, amount: float) -> bool:
        print(f"Processing ${amount} via Credit Card gateway...")
        return True
    def get_processor_name(self) -> str:
        return "Credit Card"

class PayPalProcessor(PaymentProcessor):
    def process_payment(self, amount: float) -> bool:
        print(f"Processing ${amount} via PayPal API...")
        return True
    def get_processor_name(self) -> str:
        return "PayPal"

class PaymentProcessorFactory(ABC):
    @abstractmethod
    def create_processor(self) -> PaymentProcessor:
        pass

class CreditCardProcessorFactory(PaymentProcessorFactory):
    def create_processor(self) -> PaymentProcessor:
        return CreditCardProcessor()

class PayPalProcessorFactory(PaymentProcessorFactory):
    def create_processor(self) -> PaymentProcessor:
        return PayPalProcessor()

def process_payment_with_factory(factory: PaymentProcessorFactory, amount: float):
    processor = factory.create_processor()
    print(f"Using {processor.get_processor_name()} Processor")
    return processor.process_payment(amount)

if __name__ == "__main__":
    process_payment_with_factory(CreditCardProcessorFactory(), 150.0)
    process_payment_with_factory(PayPalProcessorFactory(), 89.99)
