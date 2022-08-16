import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import C1501_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C1501   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Bose'
    header.mapModel       = 'C1501.x'
    header.mapIndex       = 61
    header.bgm            = 22
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = ['ED6_DT01/C1501._SN', 'ED6_DT01/C1501_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x64
@scena.EntryPoint('EntryPoint')
def EntryPoint():
    return (
        ScenaEntryPoint(
            dword_00        = 0xFFFE5250,
            dword_04        = 0x000017D4,
            dword_08        = 0x0001A5E0,
            word_0C         = 0x0004,
            word_0E         = 0x0087,
            dword_10        = 0,
            dword_14        = 9500,
            dword_18        = -10000,
            dword_1C        = 0,
            dword_20        = 0,
            dword_24        = 0,
            dword_28        = 2800,
            dword_2C        = 262,
            word_30         = 250,
            word_32         = 228,
            word_34         = 265,
            word_36         = 0,
            word_38         = 0,
            word_3A         = 61,
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
        ('ED6_DT07/CH01120._CH', 'ED6_DT07/CH01120P._CP'),
        ('ED6_DT09/CH10200._CH', 'ED6_DT09/CH10200P._CP'),
        ('ED6_DT09/CH10201._CH', 'ED6_DT09/CH10201P._CP'),
        ('ED6_DT07/CH00100._CH', 'ED6_DT07/CH00100P._CP'),
        ('ED6_DT07/CH00101._CH', 'ED6_DT07/CH00101P._CP'),
        ('ED6_DT07/CH00110._CH', 'ED6_DT07/CH00110P._CP'),
        ('ED6_DT07/CH00111._CH', 'ED6_DT07/CH00111P._CP'),
        ('ED6_DT07/CH00140._CH', 'ED6_DT07/CH00140P._CP'),
        ('ED6_DT07/CH00141._CH', 'ED6_DT07/CH00141P._CP'),
        ('ED6_DT09/CH10200._CH', 'ED6_DT09/CH10200P._CP'),
        ('ED6_DT09/CH10201._CH', 'ED6_DT09/CH10201P._CP'),
        ('ED6_DT09/CH10880._CH', 'ED6_DT09/CH10880P._CP'),
        ('ED6_DT09/CH10881._CH', 'ED6_DT09/CH10881P._CP'),
        ('ED6_DT09/CH11160._CH', 'ED6_DT09/CH11160P._CP'),
        ('ED6_DT09/CH11161._CH', 'ED6_DT09/CH11161P._CP'),
    ]

# id: 0x10001 offset: 0x122
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '奥维德',
            x                   = -98500,
            z                   = 4000,
            y                   = 70100,
            direction           = 225,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '魔兽',
            x                   = -97500,
            z                   = 4000,
            y                   = 71500,
            direction           = 225,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '魔兽',
            x                   = -96700,
            z                   = 4000,
            y                   = 72300,
            direction           = 225,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '魔兽',
            x                   = -95800,
            z                   = 4000,
            y                   = 73000,
            direction           = 225,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '照相机',
            x                   = 53000,
            z                   = 0,
            y                   = 33500,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '玛诺利亚海岸方向',
            x                   = -68830,
            z                   = 70,
            y                   = -31470,
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
            name                = '古罗尼山道·关所方向',
            x                   = -114600,
            z                   = 6050,
            y                   = 118780,
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

# id: 0x10002 offset: 0x202
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            name        = '',
            x           = -106080,
            z           = 6030,
            y           = 93200,
            word_0C     = 0x0000,
            word_0E     = 0x0009,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x00CD,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -104200,
            z           = 1980,
            y           = 7590,
            word_0C     = 0x0000,
            word_0E     = 0x000D,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x00CE,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -109430,
            z           = 4040,
            y           = 46760,
            word_0C     = 0x0000,
            word_0E     = 0x000B,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x00CE,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -121470,
            z           = 2040,
            y           = 22550,
            word_0C     = 0x0000,
            word_0E     = 0x0009,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x00CD,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10003 offset: 0x272
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = -109700,
            y           = 6000,
            z           = 66600,
            range       = 2000,
            dword_10    = 0x00000578,
            dword_14    = 0x00000000,
            dword_18    = 0x00010040,
            dword_1C    = 0x00000001,
        ),
    )

# id: 0x10004 offset: 0x292
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -106310,
            triggerZ            = 1990,
            triggerY            = 2710,
            triggerRange        = 1000,
            actorX              = -106430,
            actorZ              = 1990,
            actorY              = 2090,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -112480,
            triggerZ            = 2070,
            triggerY            = 63130,
            triggerRange        = 1000,
            actorX              = -112990,
            actorZ              = 2070,
            actorY              = 63430,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0004,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x2DA
@scena.Code('Init')
def Init():
    Return()

# id: 0x0001 offset: 0x2DB
@scena.Code('func_01_2DB')
def func_01_2DB():
    OP_16(0x02, 4000, -228000, -88000, 196671)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0098, 4, 0x4C4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2FF',
    )

    OP_6F(0x0000, 0)

    Jump('loc_306')

    def _loc_2FF(): pass

    label('loc_2FF')

    OP_6F(0x0000, 60)

    def _loc_306(): pass

    label('loc_306')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0098, 5, 0x4C5)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_318',
    )

    OP_6F(0x0001, 0)

    Jump('loc_31F')

    def _loc_318(): pass

    label('loc_318')

    OP_6F(0x0001, 60)

    def _loc_31F(): pass

    label('loc_31F')

    Return()

# id: 0x0002 offset: 0x320
@scena.Code('func_02_320')
def func_02_320():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_335',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('func_02_320')

    def _loc_335(): pass

    label('loc_335')

    Return()

# id: 0x0003 offset: 0x336
@scena.Code('func_03_336')
def func_03_336():
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0098, 4, 0x4C4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_42C',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0000, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(0x01FE, 1)"),
            Expr.Return,
        ),
        'loc_3AE',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            'ＥＰ填充剂',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x0098, 4, 0x4C4))

    Jump('loc_429')

    def _loc_3AE(): pass

    label('loc_3AE')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.SetColor, 0x2),
            'ＥＰ填充剂',
            (TxtCtl.SetColor, 0x0),
            '。\n',
            '不过现有的数量太多，',
            (TxtCtl.SetColor, 0x2),
            'ＥＰ填充剂',
            (TxtCtl.SetColor, 0x0),
            '不能再拿更多了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0000, 60)
    OP_70(0x0000, 0)

    def _loc_429(): pass

    label('loc_429')

    Jump('loc_462')

    def _loc_42C(): pass

    label('loc_42C')

    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱里什么东西都没有。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    WaitEffect(0x0F, 0x19)
    def _loc_462(): pass

    label('loc_462')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0004 offset: 0x470
@scena.Code('func_04_470')
def func_04_470():
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0098, 5, 0x4C5)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_566',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0001, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(0x01FE, 1)"),
            Expr.Return,
        ),
        'loc_4E8',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            'ＥＰ填充剂',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x0098, 5, 0x4C5))

    Jump('loc_563')

    def _loc_4E8(): pass

    label('loc_4E8')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.SetColor, 0x2),
            'ＥＰ填充剂',
            (TxtCtl.SetColor, 0x0),
            '。\n',
            '不过现有的数量太多，',
            (TxtCtl.SetColor, 0x2),
            'ＥＰ填充剂',
            (TxtCtl.SetColor, 0x0),
            '不能再拿更多了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0001, 60)
    OP_70(0x0001, 0)

    def _loc_563(): pass

    label('loc_563')

    Jump('loc_59C')

    def _loc_566(): pass

    label('loc_566')

    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱里什么东西都没有。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    WaitEffect(0x0F, 0x1A)
    def _loc_59C(): pass

    label('loc_59C')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
