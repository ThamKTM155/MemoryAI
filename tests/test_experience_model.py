from data_model.memory_factory import MemoryFactory

exp = MemoryFactory.create_experience(
    title="Test",
    topic="MemoryAI",
    views=100
)

print(exp.title)
print(exp.topic)
print(exp.views)