import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import C3512_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C3512   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Zeiss'
    header.mapModel       = 'C3512.x'
    header.mapIndex       = 1
    header.bgm            = 33
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x36B
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
        ('ED6_DT09/CH10710._CH', 'ED6_DT09/CH10710P._CP'),
        ('ED6_DT09/CH10711._CH', 'ED6_DT09/CH10711P._CP'),
        ('ED6_DT09/CH10720._CH', 'ED6_DT09/CH10720P._CP'),
        ('ED6_DT09/CH10721._CH', 'ED6_DT09/CH10721P._CP'),
        ('ED6_DT09/CH10730._CH', 'ED6_DT09/CH10730P._CP'),
        ('ED6_DT09/CH10731._CH', 'ED6_DT09/CH10731P._CP'),
        ('ED6_DT09/CH10740._CH', 'ED6_DT09/CH10740P._CP'),
        ('ED6_DT09/CH10741._CH', 'ED6_DT09/CH10741P._CP'),
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
            dword_10            = 6,
            chipIndex           = 6,
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
            x           = 60,
            z           = 0,
            y           = -3220,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x01F9,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10004 offset: 0x126
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x126
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 10,
            triggerZ            = 0,
            triggerY            = 700,
            triggerRange        = 1000,
            actorX              = 0,
            actorZ              = 0,
            actorY              = 0,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x14A
@scena.Code('PreInit')
def PreInit():
    Return()

# id: 0x0001 offset: 0x14B
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00B5, 3, 0x5AB)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_15D',
    )

    OP_6F(0x0000, 0)

    Jump('loc_164')

    def _loc_15D(): pass

    label('loc_15D')

    OP_6F(0x0000, 60)

    def _loc_164(): pass

    label('loc_164')

    Return()

# id: 0x0002 offset: 0x165
@scena.Code('ReInit')
def ReInit():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_17A',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('ReInit')

    def _loc_17A(): pass

    label('loc_17A')

    Return()

# id: 0x0003 offset: 0x17B
@scena.Code('func_03_17B')
def func_03_17B():
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00B5, 3, 0x5AB)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_31F',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0000, 60)
    Sleep(500)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00B5, 4, 0x5AC)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_257',
    )

    ChrSetRGBAMask(0x0008, 255, 255, 255, 0, 0)
    SetChrPos(0x0008, 0, 2000, 0, 320)
    ChrTurnDirection(0x0008, 0x0000, 0)

    @scena.Lambda('lambda_01CA')
    def lambda_01CA():
        ChrMoveTo(0x00FE, 0, 1000, 0, 1200, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_01CA)

    @scena.Lambda('lambda_01E5')
    def lambda_01E5():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 1200)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_01E5)

    ClearChrFlags(0x0008, 0x0080)

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
    Battle(0x000001F8, 0x00000000, 0x00, 0x0000, 0xFF)
    SetChrFlags(0x0008, 0x0080)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000000, 'loc_232'),
        (0x00000002, 'loc_244'),
        (0x00000001, 'loc_254'),
        (-1, 'loc_257'),
    )

    def _loc_232(): pass

    label('loc_232')

    SetScenaFlags(ScenaFlag(0x00B5, 4, 0x5AC))
    OP_6F(0x0000, 60)
    Sleep(500)

    Jump('loc_257')

    def _loc_244(): pass

    label('loc_244')

    OP_6F(0x0000, 0)
    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

    def _loc_254(): pass

    label('loc_254')

    OP_B4(0x00)

    Return()

    def _loc_257(): pass

    label('loc_257')

    If(
        (
            (Expr.Eval, "AddItem(0x0266, 1)"),
            Expr.Return,
        ),
        'loc_2AB',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '精神３',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x00B5, 3, 0x5AB))

    Jump('loc_31C')

    def _loc_2AB(): pass

    label('loc_2AB')

    FadeOut(300, 0, 100)

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.SetColor, 0x2),
            '精神３',
            (TxtCtl.SetColor, 0x0),
            '。\n',
            '不过现有的数量太多，',
            (TxtCtl.SetColor, 0x2),
            '精神３',
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

    def _loc_31C(): pass

    label('loc_31C')

    Jump('loc_355')

    def _loc_31F(): pass

    label('loc_31F')

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
    WaitEffect(0x0F, 0x30)
    def _loc_355(): pass

    label('loc_355')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
