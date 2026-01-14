from bytez import Bytez

key = "72537a96ed58d29910699530c8a21e78"
sdk = Bytez(key)

model = sdk.model("openai/gpt-5")

results = model.run([
    {"role": "user", "content": "Say hello in one sentence"}
])

print("=== ERROR ===")
print(results.error)

print("\n=== RESULT TYPE ===")
print(type(results))

print("\n=== DIR(results) ===")
print(dir(results))

print("\n=== STR(results) ===")
print(str(results))

print("\n=== REPR(results) ===")
print(repr(results))
