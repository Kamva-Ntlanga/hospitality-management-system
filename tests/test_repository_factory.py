import unittest
from factories.repository_factory import RepositoryFactory, StorageType

class TestRepositoryFactory(unittest.TestCase):
    def test_create_room_repository_memory(self):
        repo = RepositoryFactory.create_room_repository(StorageType.MEMORY)
        from repositories.inmemory.in_memory_room_repository import InMemoryRoomRepository
        self.assertIsInstance(repo, InMemoryRoomRepository)
    
    def test_create_guest_repository_memory(self):
        repo = RepositoryFactory.create_guest_repository(StorageType.MEMORY)
        from repositories.inmemory.in_memory_guest_repository import InMemoryGuestRepository
        self.assertIsInstance(repo, InMemoryGuestRepository)
    
    def test_factory_returns_different_instances(self):
        repo1 = RepositoryFactory.create_room_repository(StorageType.MEMORY)
        repo2 = RepositoryFactory.create_room_repository(StorageType.MEMORY)
        self.assertIsNot(repo1, repo2)

if __name__ == "__main__":
    unittest.main()
