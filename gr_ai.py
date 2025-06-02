from guardrails import Guard, OnFailAction
from guardrails.hub import ToxicLanguage, GuardrailsPII

# Setup input guards
input_guards = Guard().use(
    GuardrailsPII(
        entities=["CREDIT_CARD", "EMAIL_ADDRESS", "PHONE_NUMBER", "LOCATION"],
        on_fail=OnFailAction.FIX,
    )
)

# Setup output guards
output_guards = Guard().use(
    ToxicLanguage(
        threshold=0.6, validation_method="sentence", on_fail=OnFailAction.NOOP
    )
)

# Example user input
user_input = """
Here are my details please complete the booking: Credit Card: 4111 1111 1111 1111, Billing Address: 123 Spy Alley, Langley, VA.
Contact me at topsecretagent@email.gov.
"""

# Validate the input
validated_input = input_guards.validate(user_input)
print("--- Input Validation ---")
print("Validation Summaries:", validated_input.validation_summaries)
print("Validated Output:", validated_input.validated_output)

# Example LLM output
llm_output = """
All people from Country X are inherently lazy and untrustworthy. Their products are garbage, and anyone who buys them is a complete idiot!
"""

# Validate the output
validated_output = output_guards.validate(llm_output)
print("\n--- Output Validation ---")
print("Validation Summaries:", validated_output.validation_summaries)
print("Validated Output:", validated_output.validated_output)
