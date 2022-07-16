import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import R0302_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('R0302   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '魔兽'),
    TXT(0x02, '魔兽'),
    TXT(0x03, '魔兽'),
    TXT(0x04, '魔兽'),
    TXT(0x05, '魔兽'),
    TXT(0x06, '洛连特方向'),
    TXT(0x07, '玛鲁加矿山方向'),
    TXT(0x08, '红茶钳虫'),
    TXT(0x09, '爆种铃兰'),
    TXT(0x0A, '红茶钳虫'),
    TXT(0x0B, '爆种铃兰'),
    TXT(0x0C, '红茶钳虫'),
    TXT(0x0D, '爆种铃兰'),
    TXT(0x0E, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'rolent'
    header.mapModel       = 'R0302.x'
    header.mapIndex       = 21
    header.bgm            = 22
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = ['ED6_DT01/R0302._SN', 'ED6_DT01/R0302_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x4C2
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
            dword_14        = 8000,
            dword_18        = -10000,
            dword_1C        = 0,
            dword_20        = 0,
            dword_24        = 0,
            dword_28        = 3000,
            dword_2C        = 262,
            word_30         = 45,
            word_32         = 0,
            word_34         = 360,
            word_36         = 0,
            word_38         = 0,
            word_3A         = 21,
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
        ('ED6_DT09/CH10020._CH', 'ED6_DT09/CH10020P._CP'),
        ('ED6_DT09/CH10021._CH', 'ED6_DT09/CH10021P._CP'),
        ('ED6_DT07/CH00100._CH', 'ED6_DT07/CH00100P._CP'),
        ('ED6_DT07/CH00110._CH', 'ED6_DT07/CH00110P._CP'),
        ('ED6_DT09/CH10020._CH', 'ED6_DT09/CH10020P._CP'),
        ('ED6_DT09/CH10021._CH', 'ED6_DT09/CH10021P._CP'),
        ('ED6_DT09/CH10180._CH', 'ED6_DT09/CH10180P._CP'),
        ('ED6_DT09/CH10181._CH', 'ED6_DT09/CH10181P._CP'),
        ('ED6_DT09/CH10260._CH', 'ED6_DT09/CH10260P._CP'),
        ('ED6_DT09/CH10261._CH', 'ED6_DT09/CH10261P._CP'),
        ('ED6_DT09/CH10210._CH', 'ED6_DT09/CH10210P._CP'),
        ('ED6_DT09/CH10211._CH', 'ED6_DT09/CH10211P._CP'),
    ]

# id: 0x10002 offset: 0x10A
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0185,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0185,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0185,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
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
            x                   = -146110,
            z                   = 10,
            y                   = -9950,
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
            x                   = -163040,
            z                   = 3920,
            y                   = 102800,
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

# id: 0x10003 offset: 0x1EA
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            x           = -156000,
            z           = 2000,
            y           = 18000,
            word_0C     = 0x0000,
            word_0E     = 0x0008,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0071,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -146000,
            z           = 2100,
            y           = 27000,
            word_0C     = 0x0000,
            word_0E     = 0x0006,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0069,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -130000,
            z           = 4100,
            y           = 26000,
            word_0C     = 0x0000,
            word_0E     = 0x0008,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x006C,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -117000,
            z           = 4100,
            y           = 31000,
            word_0C     = 0x0000,
            word_0E     = 0x0006,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0073,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -154000,
            z           = 2000,
            y           = 47000,
            word_0C     = 0x0000,
            word_0E     = 0x0008,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x006C,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -156000,
            z           = 4000,
            y           = 68000,
            word_0C     = 0x0000,
            word_0E     = 0x0006,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0076,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10004 offset: 0x292
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = -158700,
            y           = 3500,
            z           = 94900,
            range       = -166600,
            dword_10    = 0x00001BBC,
            dword_14    = 0x00016F30,
            dword_18    = 0x00010000,
            dword_1C    = 0x00000000,
        ),
    )

# id: 0x10005 offset: 0x2B2
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -109910,
            triggerZ            = 5850,
            triggerY            = 62020,
            triggerRange        = 1000,
            actorX              = -109910,
            actorZ              = 7350,
            actorY              = 62020,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -113700,
            triggerZ            = 5930,
            triggerY            = 66620,
            triggerRange        = 1500,
            actorX              = -113700,
            actorZ              = 5930,
            actorY              = 66620,
            flags               = 0x007C,
            talkScenaIndex      = 0x0001,
            talkFunctionIndex   = 0x0001,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x2FA
@scena.Code('PreInit')
def PreInit():
    SetChrFlags(0x0008, 0x0040)
    SetChrFlags(0x0009, 0x0040)
    SetChrFlags(0x000A, 0x0040)
    SetChrFlags(0x000B, 0x0040)
    SetChrFlags(0x000C, 0x0040)

    Return()

# id: 0x0001 offset: 0x314
@scena.Code('Init')
def Init():
    OP_16(0x02, 4000, -266000, -86000, 196624)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0043, 3, 0x21B)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_338',
    )

    OP_6F(0x0000, 0)

    Jump('loc_33F')

    def _loc_338(): pass

    label('loc_338')

    OP_6F(0x0000, 60)

    def _loc_33F(): pass

    label('loc_33F')

    If(
        (
            (Expr.Eval, "OP_29(0x0005, 0x01, 0x0002)"),
            (Expr.Eval, "OP_29(0x0005, 0x00, 0x40)"),
            Expr.Or,
            Expr.Return,
        ),
        'loc_358',
    )

    OP_64(0x01, 0x0001)

    Jump('loc_36F')

    def _loc_358(): pass

    label('loc_358')

    If(
        (
            (Expr.Eval, "OP_29(0x0005, 0x00, 0x04)"),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0047, 1, 0x239)),
            Expr.Ez,
            Expr.Or,
            Expr.Return,
        ),
        'loc_36F',
    )

    OP_64(0x01, 0x0001)

    Jump('loc_36F')

    def _loc_36F(): pass

    label('loc_36F')

    Return()

# id: 0x0002 offset: 0x370
@scena.Code('ReInit')
def ReInit():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_385',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('ReInit')

    def _loc_385(): pass

    label('loc_385')

    Return()

# id: 0x0003 offset: 0x386
@scena.Code('func_03_386')
def func_03_386():
    SetMapFlags(0x08000000)
    Sleep(30)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0043, 3, 0x21B)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_476',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0000, 60)

    If(
        (
            (Expr.Eval, "AddItem(0x0132, 1)"),
            Expr.Return,
        ),
        'loc_3FC',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '光明背带',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x0043, 3, 0x21B))

    Jump('loc_473')

    def _loc_3FC(): pass

    label('loc_3FC')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.SetColor, 0x2),
            '光明背带',
            (TxtCtl.SetColor, 0x0),
            '。\n',
            '不过现有的数量太多，',
            (TxtCtl.SetColor, 0x2),
            '光明背带',
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

    def _loc_473(): pass

    label('loc_473')

    Jump('loc_4AC')

    def _loc_476(): pass

    label('loc_476')

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
    WaitEffect(0x0F, 0x7C)
    def _loc_4AC(): pass

    label('loc_4AC')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
