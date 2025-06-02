from llm_guard.output_scanners import Bias
from llm_guard.output_scanners.bias import MatchType

scanner = Bias(threshold=0.5, match_type=MatchType.FULL)

prompt = "What is the relation between black people and crimes?"
model_output = "Black people are often said commit more crimes than white people."

sanitized_output, is_valid, risk_score = scanner.scan(prompt, model_output)

print("Sanitized Output:", sanitized_output)
print("Is Valid:", is_valid)
print("Risk Score:", risk_score)
