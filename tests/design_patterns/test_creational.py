import pytest

from fuse_utils.design_patterns.creational import Singleton
from fuse_utils.design_patterns.creational import StrictSingleton


class TestSingletonClass:
    @staticmethod
    def test_singleton_can_be_instantiated():
        class SingletonClass(metaclass=Singleton):
            pass

        test_class = SingletonClass()
        assert test_class is not None

    @staticmethod
    def test_singleton_can_access_attributes():
        class SingletonClass(metaclass=Singleton):
            class_attr = "class_val"

            def __init__(self):
                self.instance_attr = "instance_val"

        assert SingletonClass.class_attr == "class_val"

        test_class = SingletonClass()
        assert test_class.instance_attr == "instance_val"
        assert test_class.class_attr == "class_val"

    @staticmethod
    def test_singleton_can_take_an_argument():
        class SingletonClass(metaclass=Singleton):
            def __init__(self, instance_val: str):
                self.instance_attr = instance_val

        test_class = SingletonClass("instance_val")
        assert test_class.instance_attr == "instance_val"

    @staticmethod
    def test_singleton_can_access_methods():
        class SingletonClass(metaclass=Singleton):
            class_attr = "class_val"

            def __init__(self):
                self.instance_attr = "instance_val"

            @staticmethod
            def static_method():
                return SingletonClass.class_attr

            @classmethod
            def class_method(cls):
                return cls.static_method()

            def instance_method(self):
                return self.instance_attr

        assert SingletonClass.static_method() == "class_val"
        assert SingletonClass.class_method() == "class_val"
        assert SingletonClass().instance_method() == "instance_val"

    @staticmethod
    def test_singleton_cannot_be_instantiated_twice():
        class SingletonClass(metaclass=Singleton):
            def __init__(self, instance_val: str):
                self.instance_attr = instance_val

        first_class = SingletonClass("first_val")
        with pytest.warns(RuntimeWarning) as record:
            second_class = SingletonClass("second_val")
        assert str(record[0].message) == (
            "Using the first instance of 'SingletonClass'"
        )

        assert first_class.instance_attr == "first_val"
        assert second_class.instance_attr == "first_val"

        first_class_id = id(first_class)
        second_class_id = id(second_class)
        assert first_class_id == second_class_id

    @staticmethod
    def test_singleton_can_set_attribute_once():
        class SingletonClass(metaclass=Singleton):
            pass

        SingletonClass.first_attr = "first_val"
        assert hasattr(SingletonClass, "first_attr")
        assert SingletonClass.first_attr == "first_val"

        test_class = SingletonClass()
        test_class.second_attr = "second_val"
        assert hasattr(test_class, "second_attr")
        assert test_class.second_attr == "second_val"

        assert hasattr(test_class, "first_attr")
        assert test_class.first_attr == "first_val"

    @staticmethod
    def test_singleton_cannot_set_attribute_more_than_once():
        class SingletonClass(metaclass=Singleton):
            class_attr = "class_val"

            def __init__(self, instance_val: str):
                self.instance_attr = instance_val

        SingletonClass.first_attr = "first_val"
        with pytest.warns(RuntimeWarning) as record:
            SingletonClass.first_attr = "second_val"
        assert str(record[0].message) == (
            "Failed to set 'second_val' to 'first_attr' for Singleton class "
            "'SingletonClass' as 'first_attr' has been set to 'first_val'"
        )
        assert SingletonClass.first_attr == "first_val"

        assert hasattr(SingletonClass, "class_attr")
        assert SingletonClass.class_attr == "class_val"
        with pytest.warns(RuntimeWarning) as record:
            SingletonClass.class_attr = "new_val"
        assert str(record[0].message) == (
            "Failed to set 'new_val' to 'class_attr' for Singleton class "
            "'SingletonClass' as 'class_attr' has been set to 'class_val'"
        )
        assert SingletonClass.class_attr == "class_val"

        # # TODO: Disable attribute reassignment for instances of metaclass
        # test_class = SingletonClass("instance_val")
        # assert hasattr(test_class, "instance_attr")
        # assert test_class.instance_attr == "instance_val"
        # with pytest.raises(AttributeError) as record:
        #     test_class.instance_attr = "new_val"
        # assert str(record[0].message) == (
        #     "Failed to set 'new_val' to 'instance_attr' for Singleton class "
        #     "'SingletonClass' as 'instance_attr' has been set to "
        #     "'instance_val'"
        # )
        # assert test_class.instance_attr == "instance_val"

    @staticmethod
    def test_singleton_instance_attributes_not_set_till_instantiated():
        class SingletonClass(metaclass=Singleton):
            def __init__(self, instance_val: str):
                self.instance_attr = instance_val

        with pytest.raises(AttributeError) as record:
            SingletonClass.instance_attr
        assert str(record.value) == (
            "type object 'SingletonClass' has no attribute 'instance_attr'"
        )
        test_class = SingletonClass("instance_val")
        assert hasattr(test_class, "instance_attr")
        assert test_class.instance_attr == "instance_val"

    # # TODO: Disable reassignment
    # @staticmethod
    # def test_singleton_cannot_reassign_attribute_within_itself():
    #     class SingletonClass(metaclass=Singleton):
    #         class_attr = "class_val"
    #         class_attr = "new_val"
    #
    #     with pytest.warns(RuntimeWarning) as record:
    #         SingletonClass
    #     assert str(record[0].message) == (
    #         "Failed to set 'new_val' to 'class_attr' for Singleton "
    #         "class 'SingletonClass' as 'class_attr' has been set to "
    #         "'class_val'"
    #     )
    #
    #     class SingletonClass(metaclass=Singleton):
    #         def __init__(self):
    #             self.instance_attr = "instance_val"
    #             self.instance_attr = "new_val"
    #
    #     with pytest.warns(RuntimeWarning) as record:
    #         SingletonClass()
    #     assert str(record[0].message) == (
    #         "Failed to set 'new_val' to 'instance_attr' for Singleton "
    #         "class 'SingletonClass' as 'instance_attr' has been set to "
    #         "'instance_val'"
    #     )

    @staticmethod
    def test_singleton_cannot_reassign_attribute_within_its_methods():
        class SingletonClass(metaclass=Singleton):
            class_attr = "class_val"

            def __init__(self):
                self.instance_attr = "instance_val"

            @staticmethod
            def static_method():
                SingletonClass.class_attr = "new_val"
                return SingletonClass.class_attr

            @classmethod
            def class_method(cls):
                cls.class_attr = "new_val"
                return cls.class_attr

            def instance_method(self):
                self.instance_attr = "new_val"
                return self.instance_attr

        assert SingletonClass.class_attr == "class_val"
        with pytest.warns(RuntimeWarning) as record:
            SingletonClass.static_method()
            SingletonClass.class_method()
        assert (
            str(record[0].message)
            == str(record[1].message)
            == (
                "Failed to set 'new_val' to 'class_attr' for Singleton class "
                "'SingletonClass' as 'class_attr' has been set to 'class_val'"
            )
        )
        assert SingletonClass.class_attr == "class_val"

        # # TODO: Disable attribute reassignment for instances of metaclass
        # test_class = SingletonClass()
        # assert test_class.instance_attr == "instance_val"
        # with pytest.warns(RuntimeWarning) as record:
        #     test_class.instance_method()
        # assert str(record[0].message) == (
        #     "Failed to set 'new_val' to 'instance_attr' for Singleton class "
        #     "'SingletonClass' as 'instance_attr' has been set to "
        #     "'instance_val'"
        # )
        # assert test_class.instance_attr == "instance_val"

    @staticmethod
    def test_singleton_cannot_redefine_methods():
        class SingletonClass(metaclass=Singleton):
            @staticmethod
            def static_method():
                pass

            @classmethod
            def class_method(cls):
                pass

            def instance_method(self):
                return self

        with pytest.warns(RuntimeWarning) as record:
            SingletonClass.static_method = lambda: True
            SingletonClass.class_method = lambda: True
        assert str(record[0].message) == (
            "Failed to redefine 'static_method' for Singleton class 'SingletonClass'"
        )
        assert str(record[1].message) == (
            "Failed to redefine 'class_method' for Singleton class 'SingletonClass'"
        )

        # # TODO: Disable method redefinition for instance methods of metaclass
        # with pytest.warns(RuntimeWarning) as record:
        #     SingletonClass().instance_method = lambda: True
        # assert str(record[0].message) == (
        #     "Failed to redefine 'instance_method' for Singleton class "
        #     "'SingletonClass'"
        # )


class TestStrictSingletonClass:
    @staticmethod
    def test_singleton_cannot_be_instantiated():
        class StrictSingletonClass(metaclass=StrictSingleton):
            pass

        with pytest.raises(RuntimeError) as record:
            StrictSingletonClass()
        assert str(record.value) == (
            "Singleton class 'StrictSingletonClass' cannot be instantiated"
        )

    @staticmethod
    def test_singleton_can_access_attributes():
        class StrictSingletonClass(metaclass=StrictSingleton):
            class_attr = "class_val"

        assert StrictSingletonClass.class_attr == "class_val"

    @staticmethod
    def test_singleton_can_access_methods():
        class StrictSingletonClass(metaclass=StrictSingleton):
            class_attr = "class_val"

            @staticmethod
            def static_method():
                return StrictSingletonClass.class_attr

            @classmethod
            def class_method(cls):
                return cls.static_method()

        assert StrictSingletonClass.static_method() == "class_val"
        assert StrictSingletonClass.class_method() == "class_val"

    @staticmethod
    def test_singleton_can_set_attribute_once():
        class StrictSingletonClass(metaclass=StrictSingleton):
            pass

        StrictSingletonClass.first_attr = "first_val"
        assert hasattr(StrictSingletonClass, "first_attr")
        assert StrictSingletonClass.first_attr == "first_val"

    @staticmethod
    def test_singleton_cannot_set_attribute_more_than_once():
        class StrictSingletonClass(metaclass=StrictSingleton):
            class_attr = "class_val"

        StrictSingletonClass.first_attr = "first_val"
        with pytest.raises(AttributeError) as record:
            StrictSingletonClass.first_attr = "second_val"
        assert str(record.value) == (
            "Failed to set 'second_val' to 'first_attr' for Singleton class "
            "'StrictSingletonClass' as 'first_attr' has been set to 'first_val'"
        )
        assert StrictSingletonClass.first_attr == "first_val"

        assert hasattr(StrictSingletonClass, "class_attr")
        assert StrictSingletonClass.class_attr == "class_val"
        with pytest.raises(AttributeError) as record:
            StrictSingletonClass.class_attr = "new_val"
        assert str(record.value) == (
            "Failed to set 'new_val' to 'class_attr' for Singleton class "
            "'StrictSingletonClass' as 'class_attr' has been set to 'class_val'"
        )
        assert StrictSingletonClass.class_attr == "class_val"

    # # TODO: Disable reassignment
    # @staticmethod
    # def test_singleton_cannot_reassign_attribute_within_itself():
    #     class StrictSingletonClass(metaclass=StrictSingleton):
    #         class_attr = "class_val"
    #         class_attr = "new_val"
    #
    #     with pytest.raises(AttributeError) as record:
    #         StrictSingletonClass
    #     assert str(record.value) == (
    #         "Failed to set 'new_val' to 'class_attr' for Singleton "
    #         "class 'StrictSingletonClass' as 'class_attr' has been set to "
    #         "'class_val'"
    #     )

    @staticmethod
    def test_singleton_cannot_reassign_attribute_within_its_methods():
        class StrictSingletonClass(metaclass=StrictSingleton):
            class_attr = "class_val"

            def __init__(self):
                self.instance_attr = "instance_val"

            @staticmethod
            def static_method():
                StrictSingletonClass.class_attr = "new_val"
                return StrictSingletonClass.class_attr

            @classmethod
            def class_method(cls):
                cls.class_attr = "new_val"
                return cls.class_attr

        assert StrictSingletonClass.class_attr == "class_val"

        with pytest.raises(AttributeError) as record:
            StrictSingletonClass.static_method()
        assert str(record.value) == (
            "Failed to set 'new_val' to 'class_attr' for Singleton class "
            "'StrictSingletonClass' as 'class_attr' has been set to 'class_val'"
        )

        with pytest.raises(AttributeError) as record:
            StrictSingletonClass.class_method()
        assert str(record.value) == (
            "Failed to set 'new_val' to 'class_attr' for Singleton class "
            "'StrictSingletonClass' as 'class_attr' has been set to 'class_val'"
        )

        assert StrictSingletonClass.class_attr == "class_val"

    @staticmethod
    def test_singleton_cannot_redefine_methods():
        class StrictSingletonClass(metaclass=StrictSingleton):
            @staticmethod
            def static_method():
                pass

            @classmethod
            def class_method(cls):
                pass

        with pytest.raises(AttributeError) as record:
            StrictSingletonClass.static_method = lambda: True
        assert str(record.value) == (
            "Failed to redefine 'static_method' for Singleton class "
            "'StrictSingletonClass'"
        )

        with pytest.raises(AttributeError) as record:
            StrictSingletonClass.class_method = lambda: True
        assert str(record.value) == (
            "Failed to redefine 'class_method' for Singleton class "
            "'StrictSingletonClass'"
        )
