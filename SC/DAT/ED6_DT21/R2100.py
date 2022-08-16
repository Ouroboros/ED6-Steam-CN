import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import R2100_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('R2100   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Ruan'
    header.mapModel       = 'R2100.x'
    header.mapIndex       = 100
    header.bgm            = 29
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
        ('ED6_DT09/CH10160._CH', 'ED6_DT09/CH10160P._CP'),
        ('ED6_DT09/CH10161._CH', 'ED6_DT09/CH10161P._CP'),
        ('ED6_DT09/CH10450._CH', 'ED6_DT09/CH10450P._CP'),
        ('ED6_DT09/CH10451._CH', 'ED6_DT09/CH10451P._CP'),
        ('ED6_DT09/CH10220._CH', 'ED6_DT09/CH10220P._CP'),
        ('ED6_DT09/CH10221._CH', 'ED6_DT09/CH10221P._CP'),
        ('ED6_DT09/CH10470._CH', 'ED6_DT09/CH10470P._CP'),
        ('ED6_DT09/CH10471._CH', 'ED6_DT09/CH10471P._CP'),
        ('ED6_DT09/CH10480._CH', 'ED6_DT09/CH10480P._CP'),
        ('ED6_DT09/CH10481._CH', 'ED6_DT09/CH10481P._CP'),
        ('ED6_DT09/CH11060._CH', 'ED6_DT09/CH11060P._CP'),
        ('ED6_DT09/CH11061._CH', 'ED6_DT09/CH11061P._CP'),
        ('ED6_DT09/CH10460._CH', 'ED6_DT09/CH10460P._CP'),
        ('ED6_DT09/CH10461._CH', 'ED6_DT09/CH10461P._CP'),
        ('ED6_DT29/CH12100._CH', 'ED6_DT29/CH12100P._CP'),
        ('ED6_DT29/CH12101._CH', 'ED6_DT29/CH12101P._CP'),
    ]

# id: 0x10001 offset: 0x12A
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '玛诺利亚村方向',
            x                   = -18570,
            z                   = -2000,
            y                   = -37710,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x00FF,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '古罗尼山道方向',
            x                   = 100500,
            z                   = -2070,
            y                   = 132300,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x00FF,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10002 offset: 0x16A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            name        = '',
            x           = 26400,
            z           = -2050,
            y           = 109110,
            word_0C     = 0x00B4,
            word_0E     = 0x0004,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x016C,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 22850,
            z           = -2020,
            y           = 80880,
            word_0C     = 0x00B4,
            word_0E     = 0x000E,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0170,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 24710,
            z           = -2070,
            y           = 44250,
            word_0C     = 0x00B4,
            word_0E     = 0x000A,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x016E,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 16680,
            z           = -2060,
            y           = 9800,
            word_0C     = 0x00B4,
            word_0E     = 0x000E,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0170,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 10660,
            z           = -1950,
            y           = 86530,
            word_0C     = 0x00B4,
            word_0E     = 0x0004,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x016C,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 53700,
            z           = -2000,
            y           = 127140,
            word_0C     = 0x00B4,
            word_0E     = 0x000E,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0170,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10003 offset: 0x212
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x212
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 35120,
            triggerZ            = -1980,
            triggerY            = 46370,
            triggerRange        = 1000,
            actorX              = 35820,
            actorZ              = -1950,
            actorY              = 46370,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0002,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x236
@scena.Code('Init')
def Init():
    Return()

# id: 0x0001 offset: 0x237
@scena.Code('func_01_237')
def func_01_237():
    OP_16(0x02, 4000, -101000, -72000, 2293803)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0260, 0, 0x1300)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_25B',
    )

    OP_6F(0x0000, 0)

    Jump('loc_262')

    def _loc_25B(): pass

    label('loc_25B')

    OP_6F(0x0000, 60)

    def _loc_262(): pass

    label('loc_262')

    ExecExpressionWithVar(
        0x3A,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    PlaySE(452, 0x01, 0x64)

    Return()

# id: 0x0002 offset: 0x271
@scena.Code('func_02_271')
def func_02_271():
    UnlockAchievement(0x02, 0x01DF, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0260, 0, 0x1300)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_34E',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0000, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['杰尼丝西装'], 1)"),
            Expr.Return,
        ),
        'loc_2E5',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['杰尼丝西装']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x0260, 0, 0x1300))

    Jump('loc_34B')

    def _loc_2E5(): pass

    label('loc_2E5')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['杰尼丝西装']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['杰尼丝西装']),
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

    def _loc_34B(): pass

    label('loc_34B')

    Jump('loc_37F')

    def _loc_34E(): pass

    label('loc_34E')

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
    def _loc_37F(): pass

    label('loc_37F')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
