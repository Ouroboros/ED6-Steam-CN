import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C1100_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C1100   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Bose'
    header.mapModel       = 'C1100.x'
    header.mapIndex       = 49
    header.bgm            = 30
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
        ('ED6_DT09/CH10300._CH', 'ED6_DT09/CH10300P._CP'),
        ('ED6_DT09/CH10301._CH', 'ED6_DT09/CH10301P._CP'),
    ]

# id: 0x10001 offset: 0xBA
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '',
            x                   = 6530,
            z                   = 1000,
            y                   = 44980,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x01C5,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10002 offset: 0xDA
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            name        = '',
            x           = 10830,
            z           = 0,
            y           = 17110,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0141,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 27540,
            z           = -500,
            y           = 33890,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0141,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 46190,
            z           = 0,
            y           = 40810,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0141,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 55780,
            z           = 0,
            y           = 26100,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0141,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 45070,
            z           = 210,
            y           = 9140,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0141,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -26630,
            z           = 0,
            y           = 11550,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0141,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -32840,
            z           = 0,
            y           = 23020,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0141,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -28410,
            z           = -500,
            y           = 39950,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0141,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -57320,
            z           = 0,
            y           = 91000,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0141,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -56950,
            z           = 0,
            y           = 108360,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0141,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -74060,
            z           = 0,
            y           = 64700,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0141,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -65650,
            z           = 0,
            y           = 65720,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0141,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -85050,
            z           = -30,
            y           = 75860,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0141,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -64209,
            z           = -480,
            y           = 36130,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0141,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -77410,
            z           = 0,
            y           = 32780,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0141,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10003 offset: 0x27E
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x27E
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 7240,
            triggerZ            = 0,
            triggerY            = 45020,
            triggerRange        = 1000,
            actorX              = 6530,
            actorZ              = 0,
            actorY              = 44980,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 20610,
            triggerZ            = 0,
            triggerY            = 49990,
            triggerRange        = 1000,
            actorX              = 21270,
            actorZ              = 0,
            actorY              = 49990,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0004,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x2C6
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0342, 6, 0x1A16)),
            Expr.Return,
        ),
        'loc_2D6',
    )

    MapSetFlags(0x10000000)
    Event(0, func_05_611)

    def _loc_2D6(): pass

    label('loc_2D6')

    Return()

# id: 0x0001 offset: 0x2D7
@scena.Code('func_01_2D7')
def func_01_2D7():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0366, 0, 0x1B30)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2E9',
    )

    OP_6F(0x0000, 0)

    Jump('loc_2F0')

    def _loc_2E9(): pass

    label('loc_2E9')

    OP_6F(0x0000, 60)

    def _loc_2F0(): pass

    label('loc_2F0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0366, 2, 0x1B32)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_302',
    )

    OP_6F(0x0001, 0)

    Jump('loc_309')

    def _loc_302(): pass

    label('loc_302')

    OP_6F(0x0001, 60)

    def _loc_309(): pass

    label('loc_309')

    Return()

# id: 0x0002 offset: 0x30A
@scena.Code('func_02_30A')
def func_02_30A():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_31F',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('func_02_30A')

    def _loc_31F(): pass

    label('loc_31F')

    Return()

# id: 0x0003 offset: 0x320
@scena.Code('func_03_320')
def func_03_320():
    UnlockAchievement(0x02, 0x0201, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0366, 0, 0x1B30)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4B8',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0000, 60)
    Sleep(500)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0366, 1, 0x1B31)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_404',
    )

    ChrSetRGBAMask(0x0008, 255, 255, 255, 0, 0)
    ChrTurnDirection(0x0008, 0x0000, 0)
    ChrMoveToRelativeAsync(0x0008, 0, 1000, 0, 0, 0x00)

    @scena.Lambda('lambda_0377')
    def lambda_0377():
        ChrMoveToRelativeAsync(0x00FE, 0, -1000, 0, 600, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0377)

    @scena.Lambda('lambda_0392')
    def lambda_0392():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 600)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_0392)

    ChrClearFlags(0x0008, 0x0080)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '魔兽出现了！',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    Battle(0x00000145, 0x00000000, 0x00, 0x0000, 0xFF)
    ChrSetFlags(0x0008, 0x0080)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000000, 'loc_3DF'),
        (0x00000002, 'loc_3F1'),
        (0x00000001, 'loc_401'),
        (-1, 'loc_404'),
    )

    def _loc_3DF(): pass

    label('loc_3DF')

    SetScenaFlags(ScenaFlag(0x0366, 1, 0x1B31))
    OP_6F(0x0000, 60)
    Sleep(500)

    Jump('loc_404')

    def _loc_3F1(): pass

    label('loc_3F1')

    OP_6F(0x0000, 0)
    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

    def _loc_401(): pass

    label('loc_401')

    OP_B4(0x00)

    Return()

    def _loc_404(): pass

    label('loc_404')

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['替身木偶'], 1)"),
            Expr.Return,
        ),
        'loc_453',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['替身木偶']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x0366, 0, 0x1B30))

    Jump('loc_4B5')

    def _loc_453(): pass

    label('loc_453')

    FadeOut(300, 0, 100)

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['替身木偶']),
            (TxtCtl.SetColor, 0x0),
            '。 \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['替身木偶']),
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

    def _loc_4B5(): pass

    label('loc_4B5')

    Jump('loc_4E7')

    def _loc_4B8(): pass

    label('loc_4B8')

    FadeOut(300, 0, 100)

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
    def _loc_4E7(): pass

    label('loc_4E7')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0004 offset: 0x4F5
@scena.Code('func_04_4F5')
def func_04_4F5():
    UnlockAchievement(0x02, 0x002A, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0366, 2, 0x1B32)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_5D2',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0001, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['爽口洋葱'], 1)"),
            Expr.Return,
        ),
        'loc_569',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['爽口洋葱']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x0366, 2, 0x1B32))

    Jump('loc_5CF')

    def _loc_569(): pass

    label('loc_569')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['爽口洋葱']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['爽口洋葱']),
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

    def _loc_5CF(): pass

    label('loc_5CF')

    Jump('loc_603')

    def _loc_5D2(): pass

    label('loc_5D2')

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
    def _loc_603(): pass

    label('loc_603')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0005 offset: 0x611
@scena.Code('func_05_611')
def func_05_611():
    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000068, 'loc_61D'),
        (-1, 'loc_629'),
    )

    def _loc_61D(): pass

    label('loc_61D')

    NewScene('ED6_DT21/C1102._SN', 104, 0, 0)
    IdleLoop()

    Jump('loc_629')

    def _loc_629(): pass

    label('loc_629')

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
