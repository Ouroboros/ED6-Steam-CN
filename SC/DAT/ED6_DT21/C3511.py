import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C3511_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C3511   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Zeiss'
    header.mapModel       = 'C3511.x'
    header.mapIndex       = 1
    header.bgm            = 33
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x64
@scena.EntryPoint('EntryPoint')
def EntryPoint():
    return (
        ScenaEntryPoint(
            dword_00        = 0x00000000,
            dword_04        = 0x00000000,
            dword_08        = 0x00001770,
            word_0C         = 0x0004,
            word_0E         = 0x0000,
            dword_10        = 0,
            dword_14        = 9500,
            dword_18        = -10000,
            dword_1C        = 0,
            dword_20        = 0,
            dword_24        = 0,
            dword_28        = 2800,
            dword_2C        = 262,
            word_30         = 45,
            word_32         = 0,
            word_34         = 360,
            word_36         = 0,
            word_38         = 0,
            word_3A         = 0,
            preInitScena    = 0x0000,
            preInitFunction = 0x0000,
            initScena       = 0x0000,
            initFunction    = 0x0001,
        ),
    )

# id: 0x10000 offset: 0xA8
@scena.ChipData('ChipData')
def ChipData():
    return [
        # (ch, cp)
        ('ED6_DT09/CH10710._CH', 'ED6_DT09/CH10710P._CP'),
        ('ED6_DT09/CH10711._CH', 'ED6_DT09/CH10711P._CP'),
        ('ED6_DT09/CH10720._CH', 'ED6_DT09/CH10720P._CP'),
        ('ED6_DT09/CH10721._CH', 'ED6_DT09/CH10721P._CP'),
        ('ED6_DT09/CH10730._CH', 'ED6_DT09/CH10730P._CP'),
        ('ED6_DT09/CH10731._CH', 'ED6_DT09/CH10731P._CP'),
        ('ED6_DT09/CH10740._CH', 'ED6_DT09/CH10740P._CP'),
        ('ED6_DT09/CH10741._CH', 'ED6_DT09/CH10741P._CP'),
        ('ED6_DT29/CH12140._CH', 'ED6_DT29/CH12140P._CP'),
        ('ED6_DT29/CH12141._CH', 'ED6_DT29/CH12141P._CP'),
    ]

# id: 0x10001 offset: 0xFA
@scena.NpcData('NpcData')
def NpcData():
    return (
    )

# id: 0x10002 offset: 0xFA
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0xFA
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0xFA
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -3400,
            triggerZ            = 0,
            triggerY            = -22930,
            triggerRange        = 1000,
            actorX              = -3400,
            actorZ              = 0,
            actorY              = -23590,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0002,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 3430,
            triggerZ            = 0,
            triggerY            = -22930,
            triggerRange        = 1000,
            actorX              = 3490,
            actorZ              = 0,
            actorY              = -23630,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 4760,
            triggerZ            = 0,
            triggerY            = 22800,
            triggerRange        = 1000,
            actorX              = 4760,
            actorZ              = 0,
            actorY              = 23420,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0004,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -4540,
            triggerZ            = 0,
            triggerY            = 22820,
            triggerRange        = 1000,
            actorX              = -4630,
            actorZ              = 0,
            actorY              = 23480,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0005,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x18A
@scena.Code('Init')
def Init():
    Return()

# id: 0x0001 offset: 0x18B
@scena.Code('func_01_18B')
def func_01_18B():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02A8, 0, 0x1540)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_19D',
    )

    OP_6F(0x0000, 0)

    Jump('loc_1A4')

    def _loc_19D(): pass

    label('loc_19D')

    OP_6F(0x0000, 60)

    def _loc_1A4(): pass

    label('loc_1A4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02A8, 1, 0x1541)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1B6',
    )

    OP_6F(0x0001, 0)

    Jump('loc_1BD')

    def _loc_1B6(): pass

    label('loc_1B6')

    OP_6F(0x0001, 60)

    def _loc_1BD(): pass

    label('loc_1BD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02A8, 2, 0x1542)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1CF',
    )

    OP_6F(0x0002, 0)

    Jump('loc_1D6')

    def _loc_1CF(): pass

    label('loc_1CF')

    OP_6F(0x0002, 60)

    def _loc_1D6(): pass

    label('loc_1D6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02A8, 3, 0x1543)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1E8',
    )

    OP_6F(0x0003, 0)

    Jump('loc_1EF')

    def _loc_1E8(): pass

    label('loc_1E8')

    OP_6F(0x0003, 60)

    def _loc_1EF(): pass

    label('loc_1EF')

    Return()

# id: 0x0002 offset: 0x1F0
@scena.Code('func_02_1F0')
def func_02_1F0():
    UnlockAchievement(0x02, 0x00C7, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02A8, 0, 0x1540)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2CD',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0000, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['复苏药'], 1)"),
            Expr.Return,
        ),
        'loc_264',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['复苏药']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x02A8, 0, 0x1540))

    Jump('loc_2CA')

    def _loc_264(): pass

    label('loc_264')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['复苏药']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['复苏药']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0000, 60)
    OP_70(0x0000, 0)

    def _loc_2CA(): pass

    label('loc_2CA')

    Jump('loc_2FE')

    def _loc_2CD(): pass

    label('loc_2CD')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱中什么都没有。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    def _loc_2FE(): pass

    label('loc_2FE')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0003 offset: 0x30C
@scena.Code('func_03_30C')
def func_03_30C():
    UnlockAchievement(0x02, 0x00C8, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02A8, 1, 0x1541)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3E9',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0001, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['中回复药'], 1)"),
            Expr.Return,
        ),
        'loc_380',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['中回复药']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x02A8, 1, 0x1541))

    Jump('loc_3E6')

    def _loc_380(): pass

    label('loc_380')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['中回复药']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['中回复药']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0001, 60)
    OP_70(0x0001, 0)

    def _loc_3E6(): pass

    label('loc_3E6')

    Jump('loc_41A')

    def _loc_3E9(): pass

    label('loc_3E9')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱中什么都没有。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    def _loc_41A(): pass

    label('loc_41A')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0004 offset: 0x428
@scena.Code('func_04_428')
def func_04_428():
    UnlockAchievement(0x02, 0x00C9, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02A8, 2, 0x1542)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_505',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0002, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['EP填充剂Ⅰ'], 1)"),
            Expr.Return,
        ),
        'loc_49C',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['EP填充剂Ⅰ']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x02A8, 2, 0x1542))

    Jump('loc_502')

    def _loc_49C(): pass

    label('loc_49C')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['EP填充剂Ⅰ']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['EP填充剂Ⅰ']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0002, 60)
    OP_70(0x0002, 0)

    def _loc_502(): pass

    label('loc_502')

    Jump('loc_536')

    def _loc_505(): pass

    label('loc_505')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱中什么都没有。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    def _loc_536(): pass

    label('loc_536')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0005 offset: 0x544
@scena.Code('func_05_544')
def func_05_544():
    UnlockAchievement(0x02, 0x00CA, 0x00)
    MapSetFlags(0x08000000)
    FadeOut(300, 0, 100)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02A8, 3, 0x1543)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_662',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0003, 30)
    OP_73(0x0003)
    OP_6F(0x0003, 30)
    AddSepith(0x00, 20)
    AddSepith(0x01, 20)
    AddSepith(0x02, 20)
    AddSepith(0x03, 20)
    AddSepith(0x04, 20)
    AddSepith(0x05, 20)
    AddSepith(0x06, 20)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '#56I地之耀晶片×２０\n',
            (TxtCtl.SetColor, 0x2),
            '#57I水之耀晶片×２０\n',
            (TxtCtl.SetColor, 0x2),
            '#58I火之耀晶片×２０\n',
            (TxtCtl.SetColor, 0x2),
            '#59I风之耀晶片×２０\n',
            (TxtCtl.SetColor, 0x2),
            '#62I时之耀晶片×２０\n',
            (TxtCtl.SetColor, 0x2),
            '#60I空之耀晶片×２０\n',
            (TxtCtl.SetColor, 0x2),
            '#61I幻之耀晶片×２０\n',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    SetScenaFlags(ScenaFlag(0x02A8, 3, 0x1543))

    Jump('loc_67C')

    def _loc_662(): pass

    label('loc_662')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱中什么都没有。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    def _loc_67C(): pass

    label('loc_67C')

    FadeIn(300, 0)
    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
