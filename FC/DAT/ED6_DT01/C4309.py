import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import C4309_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C4309   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Grancel'
    header.mapModel       = 'C4309.x'
    header.mapIndex       = 1
    header.bgm            = 35
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x858
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
        ('ED6_DT09/CH11090._CH', 'ED6_DT09/CH11090P._CP'),
        ('ED6_DT09/CH11091._CH', 'ED6_DT09/CH11091P._CP'),
        ('ED6_DT09/CH11100._CH', 'ED6_DT09/CH11100P._CP'),
        ('ED6_DT09/CH11101._CH', 'ED6_DT09/CH11101P._CP'),
        ('ED6_DT09/CH10940._CH', 'ED6_DT09/CH10940P._CP'),
        ('ED6_DT09/CH10941._CH', 'ED6_DT09/CH10941P._CP'),
        ('ED6_DT09/CH10920._CH', 'ED6_DT09/CH10920P._CP'),
        ('ED6_DT09/CH10921._CH', 'ED6_DT09/CH10921P._CP'),
    ]

# id: 0x10002 offset: 0xEA
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x01C5,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10003 offset: 0x10A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            x           = 184410,
            z           = 0,
            y           = -20050,
            word_0C     = 0x00B4,
            word_0E     = 0x0006,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0292,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 195930,
            z           = 0,
            y           = -169030,
            word_0C     = 0x00B4,
            word_0E     = 0x0006,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0292,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 122910,
            z           = 0,
            y           = -99250,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x028E,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -97750,
            z           = 0,
            y           = -163430,
            word_0C     = 0x00B4,
            word_0E     = 0x0006,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0292,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10004 offset: 0x17A
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x17A
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 23740,
            triggerZ            = 0,
            triggerY            = -215090,
            triggerRange        = 1000,
            actorX              = 22960,
            actorZ              = 0,
            actorY              = -215120,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 48860,
            triggerZ            = 0,
            triggerY            = -93440,
            triggerRange        = 1000,
            actorX              = 48990,
            actorZ              = 0,
            actorY              = -92760,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0004,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 92930,
            triggerZ            = 0,
            triggerY            = -58330,
            triggerRange        = 1000,
            actorX              = 92950,
            actorZ              = 0,
            actorY              = -59080,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0005,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 264940,
            triggerZ            = 0,
            triggerY            = -107480,
            triggerRange        = 1000,
            actorX              = 264970,
            actorZ              = 0,
            actorY              = -106820,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0006,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x20A
@scena.Code('PreInit')
def PreInit():
    Return()

# id: 0x0001 offset: 0x20B
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00D5, 0, 0x6A8)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_21D',
    )

    OP_6F(0x0000, 0)

    Jump('loc_224')

    def _loc_21D(): pass

    label('loc_21D')

    OP_6F(0x0000, 60)

    def _loc_224(): pass

    label('loc_224')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00D5, 2, 0x6AA)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_236',
    )

    OP_6F(0x0001, 0)

    Jump('loc_23D')

    def _loc_236(): pass

    label('loc_236')

    OP_6F(0x0001, 60)

    def _loc_23D(): pass

    label('loc_23D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00D5, 3, 0x6AB)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_24F',
    )

    OP_6F(0x0002, 0)

    Jump('loc_256')

    def _loc_24F(): pass

    label('loc_24F')

    OP_6F(0x0002, 60)

    def _loc_256(): pass

    label('loc_256')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00D5, 4, 0x6AC)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_268',
    )

    OP_6F(0x0003, 0)

    Jump('loc_26F')

    def _loc_268(): pass

    label('loc_268')

    OP_6F(0x0003, 60)

    def _loc_26F(): pass

    label('loc_26F')

    Return()

# id: 0x0002 offset: 0x270
@scena.Code('ReInit')
def ReInit():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_285',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('ReInit')

    def _loc_285(): pass

    label('loc_285')

    Return()

# id: 0x0003 offset: 0x286
@scena.Code('func_03_286')
def func_03_286():
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00D5, 0, 0x6A8)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_434',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0000, 60)
    Sleep(500)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00D5, 1, 0x6A9)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_366',
    )

    ChrSetRGBAMask(0x0008, 255, 255, 255, 0, 0)
    SetChrPos(0x0008, 22960, 1500, -215120, 320)
    ChrTurnDirection(0x0008, 0x0000, 0)

    @scena.Lambda('lambda_02D5')
    def lambda_02D5():
        ChrMoveTo(0x00FE, 22960, 1000, -215120, 1200, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_02D5)

    @scena.Lambda('lambda_02F0')
    def lambda_02F0():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 1200)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_02F0)

    ClearChrFlags(0x0008, 0x0080)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '机械人形出现了！',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    Battle(0x00000311, 0x00000000, 0x00, 0x0000, 0xFF)
    SetChrFlags(0x0008, 0x0080)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000000, 'loc_341'),
        (0x00000002, 'loc_353'),
        (0x00000001, 'loc_363'),
        (-1, 'loc_366'),
    )

    def _loc_341(): pass

    label('loc_341')

    SetScenaFlags(ScenaFlag(0x00D5, 1, 0x6A9))
    OP_6F(0x0000, 60)
    Sleep(500)

    Jump('loc_366')

    def _loc_353(): pass

    label('loc_353')

    OP_6F(0x0000, 0)
    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

    def _loc_363(): pass

    label('loc_363')

    OP_B4(0x00)

    Return()

    def _loc_366(): pass

    label('loc_366')

    If(
        (
            (Expr.Eval, "AddItem(0x011A, 1)"),
            Expr.Return,
        ),
        'loc_3BC',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '风神之靴',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x00D5, 0, 0x6A8))

    Jump('loc_431')

    def _loc_3BC(): pass

    label('loc_3BC')

    FadeOut(300, 0, 100)

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.SetColor, 0x2),
            '风神之靴',
            (TxtCtl.SetColor, 0x0),
            '。\n',
            '不过现有的数量太多，',
            (TxtCtl.SetColor, 0x2),
            '风神之靴',
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

    def _loc_431(): pass

    label('loc_431')

    Jump('loc_46A')

    def _loc_434(): pass

    label('loc_434')

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
    WaitEffect(0x0F, 0x65)
    def _loc_46A(): pass

    label('loc_46A')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0004 offset: 0x478
@scena.Code('func_04_478')
def func_04_478():
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00D5, 2, 0x6AA)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_57A',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0001, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(0x01FF, 1)"),
            Expr.Return,
        ),
        'loc_4F4',
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
            'ＥＰ改良填充剂',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x00D5, 2, 0x6AA))

    Jump('loc_577')

    def _loc_4F4(): pass

    label('loc_4F4')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.SetColor, 0x2),
            'ＥＰ改良填充剂',
            (TxtCtl.SetColor, 0x0),
            '。\n',
            '不过现有的数量太多，',
            (TxtCtl.SetColor, 0x2),
            'ＥＰ改良填充剂',
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

    def _loc_577(): pass

    label('loc_577')

    Jump('loc_5B0')

    def _loc_57A(): pass

    label('loc_57A')

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
    WaitEffect(0x0F, 0x66)
    def _loc_5B0(): pass

    label('loc_5B0')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0005 offset: 0x5BE
@scena.Code('func_05_5BE')
def func_05_5BE():
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00D5, 3, 0x6AB)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_6C0',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0002, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(0x01FF, 1)"),
            Expr.Return,
        ),
        'loc_63A',
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
            'ＥＰ改良填充剂',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x00D5, 3, 0x6AB))

    Jump('loc_6BD')

    def _loc_63A(): pass

    label('loc_63A')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.SetColor, 0x2),
            'ＥＰ改良填充剂',
            (TxtCtl.SetColor, 0x0),
            '。\n',
            '不过现有的数量太多，',
            (TxtCtl.SetColor, 0x2),
            'ＥＰ改良填充剂',
            (TxtCtl.SetColor, 0x0),
            '不能再拿更多了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0002, 60)
    OP_70(0x0002, 0)

    def _loc_6BD(): pass

    label('loc_6BD')

    Jump('loc_6F6')

    def _loc_6C0(): pass

    label('loc_6C0')

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
    WaitEffect(0x0F, 0x67)
    def _loc_6F6(): pass

    label('loc_6F6')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0006 offset: 0x704
@scena.Code('func_06_704')
def func_06_704():
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00D5, 4, 0x6AC)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_806',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0003, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(0x01FF, 1)"),
            Expr.Return,
        ),
        'loc_780',
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
            'ＥＰ改良填充剂',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x00D5, 4, 0x6AC))

    Jump('loc_803')

    def _loc_780(): pass

    label('loc_780')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.SetColor, 0x2),
            'ＥＰ改良填充剂',
            (TxtCtl.SetColor, 0x0),
            '。\n',
            '不过现有的数量太多，',
            (TxtCtl.SetColor, 0x2),
            'ＥＰ改良填充剂',
            (TxtCtl.SetColor, 0x0),
            '不能再拿更多了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0003, 60)
    OP_70(0x0003, 0)

    def _loc_803(): pass

    label('loc_803')

    Jump('loc_83C')

    def _loc_806(): pass

    label('loc_806')

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
    WaitEffect(0x0F, 0x68)
    def _loc_83C(): pass

    label('loc_83C')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
