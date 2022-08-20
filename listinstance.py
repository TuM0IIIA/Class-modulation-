#!python

# File listinstance.py (2.X + 3.X)

class ListInstance:
    """
    Mix-in class that provides a formatted print() or str() of instances via
    inheritance of __str__ coded here; displays instance attrs only; self is
    instance of lowest class; __X names avoid clashing with client's attrs

Use dir() to collect both instance attrs and names inherited from
 its classes;
 Python 3.X shows more names than 2.X because of the
 implied object superclass in the new-style class model;
 getattr()
fetches inherited names not in self.__dict__;
use __str__, not  __repr__, or else this loops when printing bound methods!
------------------------------------------------------------------------------
Как одно возможное усовершенствование, направленное на решение проблемы с
ростом количества унаследованных имен и длинных значений,
 в следующей альтернативной версии__ attrnames из файла listinherited2 .ру в
пакете примеров для книги имена с двумя символами подчеркивания группируются отдельно,
а переносы строк для длинных значений атрибутов сводятся к минимуму. Обратите внимание на
отмену % с помощью % %, так что остается только один символ для финальной операции форматирования:

    def __attrnames(self):
        result = ' '
        for attr in dir(self):  # Instance dir()
            if attr[:2] == '__' and attr[-2:] == '__':  # Skip internals
                result += '\t{}\n'.format(attr)
            else:
                result += '\t{}={}\n'.format(attr, getattr(self, attr))
        return result
"""

    def __attrnames(self, indent=' ' * 4):
        result = 'Unders%s\n%s%%s\nOthers%s\n' % ('-' * 77, indent, '-' * 77)
        unders = []
        for attr in dir(self):  # Instance dir()
            if attr[:2] == '__' and attr[-2:] == '__':  # Skip internals
                unders.append(attr)
            else:
                display = str(getattr(self, attr))[:82 - (len(indent) + len(attr))]
                result += '%s%s=%s\n' % (indent, attr, display)
        return result % ', '.join(unders)

    def __str__(self):
        return '< Instance of {}, address {}:\n{} >'.format(
                self.__class__.__name__,  # My class's name
                id(self),  # My address
                self.__attrnames())  # name=value lis


"""

    def __attrnames(self):
        result = ' '
        for attr in sorted(self.__dict__):
            result += '\t{}={}\n' .format (attr, self.__dict__[attr])
        return result

    def __str__(self):
        return '< Instance of {}, address {}:\n{} >' .format(
            self.__class__.__name__,  # My class's name
            id(self),  # My address
            self.__attrnames())  # name=value list
            
В том виде, как есть, наш подмешиваемый класс Listerinstance отображает
только атрибуты экземпляра (т.е. имена, присоединенные к самому объекту экземпляра). 
Тем не менее, класс легко расширить для отображения всех атрибутов, доступных
из экземпляра — собственных и унаследованных из его классов. Трюк предусматривает
применение встроенной функции dir вместо просмотра словаря__ diet__ ; словарь
хранит только атрибуты экземпляра, но функция также собирает все унаследованные
атрибуты в Python 2.2 и последующих версиях.
--------------------------------------------------------------------------------------------
__attrnames method here more concisely with a generator expression that is triggered by the string join method,
 but it’s arguably less clear—expressions that wrap lines like this should generally make you consider simpler coding
alternatives:

    def __attrnames(self):
        return ’ ’ .join(’\t{} = {} \n'.format (attr, self.__diet__ [attr])
        for attr in sorted(self.__diet__))
"""

if __name__ == '__main__':
    import testmixin

    testmixin.tester(ListInstance)
