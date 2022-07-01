import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C5410_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C5410   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '哨兵570（蓝）'),
    TXT(0x02, '目标探索者'),
    TXT(0x03, '目标探索者'),
    TXT(0x04, '哨兵235（红）'),
    TXT(0x05, '哨兵570（蓝）'),
    TXT(0x06, '目标探索者'),
    TXT(0x07, '目标探索者'),
    TXT(0x08, '哨兵235（红）'),
    TXT(0x09, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Other'
    header.mapModel       = 'C5410.x'
    header.mapIndex       = 1
    header.bgm            = 28
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x55C
@scena.StringTable('StringTable')
def StringTable():
    return stringTable

# id: 0x10000 offset: 0x64
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

# id: 0x10001 offset: 0xA8
@scena.ChipData('ChipData')
def ChipData():
    return [
        # (ch, cp)
        ('ED6_DT29/CH12570._CH', 'ED6_DT29/CH12570P._CP'),
        ('ED6_DT29/CH12571._CH', 'ED6_DT29/CH12571P._CP'),
        ('ED6_DT29/CH12350._CH', 'ED6_DT29/CH12350P._CP'),
        ('ED6_DT29/CH12351._CH', 'ED6_DT29/CH12351P._CP'),
        ('ED6_DT29/CH12580._CH', 'ED6_DT29/CH12580P._CP'),
        ('ED6_DT29/CH12581._CH', 'ED6_DT29/CH12581P._CP'),
        ('ED6_DT29/CH12320._CH', 'ED6_DT29/CH12320P._CP'),
        ('ED6_DT29/CH12321._CH', 'ED6_DT29/CH12321P._CP'),
    ]

# id: 0x10002 offset: 0xEA
@scena.NpcData('NpcData')
def NpcData():
    return (
    )

# id: 0x10003 offset: 0xEA
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            x           = -64330,
            z           = 1000,
            y           = 62450,
            word_0C     = 0x0000,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0424,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -45060,
            z           = 0,
            y           = 5510,
            word_0C     = 0x0000,
            word_0E     = 0x0004,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0428,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -125030,
            z           = 0,
            y           = -45280,
            word_0C     = 0x0000,
            word_0E     = 0x0004,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0428,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -113980,
            z           = 1000,
            y           = -111570,
            word_0C     = 0x0000,
            word_0E     = 0x0002,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0427,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -64330,
            z           = 1000,
            y           = 62450,
            word_0C     = 0x0000,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x042D,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -45060,
            z           = 0,
            y           = 5510,
            word_0C     = 0x0000,
            word_0E     = 0x0004,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0431,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -125030,
            z           = 0,
            y           = -45280,
            word_0C     = 0x0000,
            word_0E     = 0x0004,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0431,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -113980,
            z           = 1000,
            y           = -111570,
            word_0C     = 0x0000,
            word_0E     = 0x0002,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0430,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10004 offset: 0x1CA
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = -127440,
            y           = 0,
            z           = -25200,
            range       = -122190,
            dword_10    = 0x000007D0,
            dword_14    = 0xFFFF8F80,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000004,
        ),
        ScenaEventData(
            x           = -127660,
            y           = 0,
            z           = -57300,
            range       = -122030,
            dword_10    = 0x000007D0,
            dword_14    = 0xFFFF13AC,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000005,
        ),
        ScenaEventData(
            x           = -92800,
            y           = 0,
            z           = -166990,
            range       = -89100,
            dword_10    = 0x000007D0,
            dword_14    = 0xFFFD919E,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000006,
        ),
    )

# id: 0x10005 offset: 0x22A
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -81710,
            triggerZ            = 0,
            triggerY            = -17950,
            triggerRange        = 1000,
            actorX              = -81000,
            actorZ              = 0,
            actorY              = -18020,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0002,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x24E
@scena.Code('PreInit')
def PreInit():
    Return()

# id: 0x0001 offset: 0x24F
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_26D',
    )

    ExecExpressionWithVar(
        0x3B,
        (
            (Expr.PushLong, 0x227),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithVar(
        0x3C,
        (
            (Expr.PushLong, 0x10A),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_26D(): pass

    label('loc_26D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03A7, 2, 0x1D3A)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_27F',
    )

    OP_6F(0x0013, 0)

    Jump('loc_286')

    def _loc_27F(): pass

    label('loc_27F')

    OP_6F(0x0013, 60)

    def _loc_286(): pass

    label('loc_286')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2A9',
    )

    SetChrFlags(0x0008, 0x0080)
    SetChrFlags(0x0009, 0x0080)
    SetChrFlags(0x000A, 0x0080)
    SetChrFlags(0x000B, 0x0080)

    Jump('loc_2BD')

    def _loc_2A9(): pass

    label('loc_2A9')

    SetChrFlags(0x000C, 0x0080)
    SetChrFlags(0x000D, 0x0080)
    SetChrFlags(0x000E, 0x0080)
    SetChrFlags(0x000F, 0x0080)

    def _loc_2BD(): pass

    label('loc_2BD')

    Call(0, 0x0003)

    Return()

# id: 0x0002 offset: 0x2C2
@scena.Code('ReInit')
def ReInit():
    UnlockAchievement(0x02, 0x7F, 0x01, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03A7, 2, 0x1D3A)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_39F',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0013, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['替身木偶'], 1)"),
            Expr.Return,
        ),
        'loc_336',
    )

    FadeOut(300, 0, 100)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

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
    OP_A2(0x1D3A)

    Jump('loc_39C')

    def _loc_336(): pass

    label('loc_336')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['替身木偶']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
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
    OP_22(0x002C, 0x00, 0x64)
    OP_6F(0x0013, 60)
    OP_70(0x0013, 0x00000000)

    def _loc_39C(): pass

    label('loc_39C')

    Jump('loc_3D0')

    def _loc_39F(): pass

    label('loc_39F')

    FadeOut(300, 0, 100)
    SetChrName('')

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
    def _loc_3D0(): pass

    label('loc_3D0')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0003 offset: 0x3DE
@scena.Code('func_03_3DE')
def func_03_3DE():
    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x9),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_3EB',
    )

    Return()

    def _loc_3EB(): pass

    label('loc_3EB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0394, 6, 0x1CA6)),
            Expr.Return,
        ),
        'loc_420',
    )

    OP_6F(0x0000, 100)
    OP_72(0x0000, 0x0002)
    OP_BE(0x00, 0x01, 0x0002, 0x0064, 0x0000, 0x02, -127510, -1000, -25720, -122680, 2000, -28500)

    def _loc_420(): pass

    label('loc_420')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0394, 7, 0x1CA7)),
            Expr.Return,
        ),
        'loc_455',
    )

    OP_6F(0x0001, 100)
    OP_72(0x0001, 0x0002)
    OP_BE(0x01, 0x01, 0x0002, 0x0064, 0x0000, 0x02, -127750, -1000, -57600, -122480, 2000, -60300)

    def _loc_455(): pass

    label('loc_455')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0395, 0, 0x1CA8)),
            Expr.Return,
        ),
        'loc_48A',
    )

    OP_6F(0x0002, 100)
    OP_72(0x0002, 0x0002)
    OP_BE(0x02, 0x01, 0x0002, 0x0064, 0x0000, 0x02, -92500, -1000, -167010, -89100, 2000, -159530)

    def _loc_48A(): pass

    label('loc_48A')

    Return()

# id: 0x0004 offset: 0x48B
@scena.Code('func_04_48B')
def func_04_48B():
    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x9),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_498',
    )

    Return()

    def _loc_498(): pass

    label('loc_498')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0394, 6, 0x1CA6)),
            Expr.Return,
        ),
        'loc_4A0',
    )

    Return()

    def _loc_4A0(): pass

    label('loc_4A0')

    EventBegin(0x02)
    OP_22(0x006B, 0x00, 0x64)
    OP_6F(0x0000, 0)
    OP_70(0x0000, 0x00000064)
    Sleep(900)

    OP_22(0x009D, 0x00, 0x64)
    OP_73(0x0000)
    OP_A2(0x1CA6)
    Call(0, 0x0003)
    EventEnd(0x03)

    Return()

# id: 0x0005 offset: 0x4CC
@scena.Code('func_05_4CC')
def func_05_4CC():
    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x9),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_4D9',
    )

    Return()

    def _loc_4D9(): pass

    label('loc_4D9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0394, 7, 0x1CA7)),
            Expr.Return,
        ),
        'loc_4E1',
    )

    Return()

    def _loc_4E1(): pass

    label('loc_4E1')

    EventBegin(0x02)
    OP_22(0x006B, 0x00, 0x64)
    OP_6F(0x0001, 0)
    OP_70(0x0001, 0x00000064)
    Sleep(900)

    OP_22(0x009D, 0x00, 0x64)
    OP_73(0x0001)
    OP_A2(0x1CA7)
    Call(0, 0x0003)
    EventEnd(0x03)

    Return()

# id: 0x0006 offset: 0x50D
@scena.Code('func_06_50D')
def func_06_50D():
    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x9),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_51A',
    )

    Return()

    def _loc_51A(): pass

    label('loc_51A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0395, 0, 0x1CA8)),
            Expr.Return,
        ),
        'loc_522',
    )

    Return()

    def _loc_522(): pass

    label('loc_522')

    EventBegin(0x02)
    OP_22(0x006B, 0x00, 0x64)
    OP_6F(0x0002, 0)
    OP_70(0x0002, 0x00000064)
    Sleep(900)

    OP_22(0x009D, 0x00, 0x64)
    OP_73(0x0002)
    OP_A2(0x1CA8)
    Call(0, 0x0003)
    EventEnd(0x03)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
