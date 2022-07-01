import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C5317_1_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C5317_1 ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Other'
    header.mapModel       = 'C5317.x'
    header.mapIndex       = 1
    header.bgm            = 10
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = ['ED6_DT21/C5317._SN', 'ED6_DT21/C5317_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x5050
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
    ]

# id: 0x10002 offset: 0xA8
@scena.NpcData('NpcData')
def NpcData():
    return (
    )

# id: 0x10003 offset: 0xA8
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0xA8
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0xA8
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0xA8
@scena.Code('PreInit')
def PreInit():
    Return()

# id: 0x0001 offset: 0xA9
@scena.Code('Init')
def Init():
    Return()

# id: 0x0002 offset: 0xAA
@scena.Code('ReInit')
def ReInit():
    EventBegin(0x00)
    OP_C4(0x01, 0x00000010)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_C7',
    )

    Call(0, 0x0021)
    Call(0, 0x0022)

    def _loc_C7(): pass

    label('loc_C7')

    OP_D2(0x002601E2, 0x002601E7, 0x00)
    OP_D2(0x002601EC, 0x002601F1, 0x01)
    OP_D2(0x002601ED, 0x002601F2, 0x02)
    OP_D2(0x00270110, 0x00270120, 0x03)
    OP_D2(0x0027034E, 0x0027035E, 0x06)
    OP_D2(0x00270019, 0x0027001D, 0x07)

    Switch(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            Expr.Return,
        ),
        (0x00000002, 'loc_134'),
        (0x00000005, 'loc_141'),
        (0x00000003, 'loc_14E'),
        (0x00000004, 'loc_15B'),
        (0x00000006, 'loc_168'),
        (0x00000007, 'loc_175'),
        (0x00000008, 'loc_182'),
        (0x0000000A, 'loc_18F'),
        (0x0000000E, 'loc_19C'),
        (0x0000000F, 'loc_1A9'),
        (-1, 'loc_1B6'),
    )

    def _loc_134(): pass

    label('loc_134')

    OP_D2(0x000701D0, 0x000701DC, 0x0B)

    Jump('loc_1B6')

    def _loc_141(): pass

    label('loc_141')

    OP_D2(0x00070218, 0x00070224, 0x0B)

    Jump('loc_1B6')

    def _loc_14E(): pass

    label('loc_14E')

    OP_D2(0x000701E8, 0x000701F4, 0x0B)

    Jump('loc_1B6')

    def _loc_15B(): pass

    label('loc_15B')

    OP_D2(0x0027036E, 0x0027037B, 0x0B)

    Jump('loc_1B6')

    def _loc_168(): pass

    label('loc_168')

    OP_D2(0x00070230, 0x0007023C, 0x0B)

    Jump('loc_1B6')

    def _loc_175(): pass

    label('loc_175')

    OP_D2(0x00070248, 0x00070254, 0x0B)

    Jump('loc_1B6')

    def _loc_182(): pass

    label('loc_182')

    OP_D2(0x00270176, 0x00270183, 0x0B)

    Jump('loc_1B6')

    def _loc_18F(): pass

    label('loc_18F')

    OP_D2(0x000702B4, 0x000702BB, 0x0B)

    Jump('loc_1B6')

    def _loc_19C(): pass

    label('loc_19C')

    OP_D2(0x002702D6, 0x002702E0, 0x0B)

    Jump('loc_1B6')

    def _loc_1A9(): pass

    label('loc_1A9')

    OP_D2(0x002702C2, 0x002702CC, 0x0B)

    Jump('loc_1B6')

    def _loc_1B6(): pass

    label('loc_1B6')

    Switch(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            Expr.Return,
        ),
        (0x00000002, 'loc_1E7'),
        (0x00000005, 'loc_1F4'),
        (0x00000003, 'loc_201'),
        (0x00000004, 'loc_20E'),
        (0x00000006, 'loc_21B'),
        (0x00000007, 'loc_228'),
        (0x00000008, 'loc_235'),
        (0x0000000A, 'loc_242'),
        (0x0000000E, 'loc_24F'),
        (0x0000000F, 'loc_25C'),
        (-1, 'loc_269'),
    )

    def _loc_1E7(): pass

    label('loc_1E7')

    OP_D2(0x000701D0, 0x000701DC, 0x0D)

    Jump('loc_269')

    def _loc_1F4(): pass

    label('loc_1F4')

    OP_D2(0x00070218, 0x00070224, 0x0D)

    Jump('loc_269')

    def _loc_201(): pass

    label('loc_201')

    OP_D2(0x000701E8, 0x000701F4, 0x0D)

    Jump('loc_269')

    def _loc_20E(): pass

    label('loc_20E')

    OP_D2(0x0027036E, 0x0027037B, 0x0D)

    Jump('loc_269')

    def _loc_21B(): pass

    label('loc_21B')

    OP_D2(0x00070230, 0x0007023C, 0x0D)

    Jump('loc_269')

    def _loc_228(): pass

    label('loc_228')

    OP_D2(0x00070248, 0x00070254, 0x0D)

    Jump('loc_269')

    def _loc_235(): pass

    label('loc_235')

    OP_D2(0x00270176, 0x00270183, 0x0D)

    Jump('loc_269')

    def _loc_242(): pass

    label('loc_242')

    OP_D2(0x000702B4, 0x000702BB, 0x0D)

    Jump('loc_269')

    def _loc_24F(): pass

    label('loc_24F')

    OP_D2(0x002702D6, 0x002702E0, 0x0D)

    Jump('loc_269')

    def _loc_25C(): pass

    label('loc_25C')

    OP_D2(0x002702C2, 0x002702CC, 0x0D)

    Jump('loc_269')

    def _loc_269(): pass

    label('loc_269')

    OP_D2(0x00270292, 0x0027029C, 0x0F)
    OP_D2(0x00270296, 0x002702A0, 0x10)
    OP_D2(0x002601E6, 0x002601EB, 0x11)
    OP_D2(0x002701D3, 0x002701D8, 0x12)
    OP_D2(0x00270445, 0x00270447, 0x13)
    OP_D2(0x002701D2, 0x002701D7, 0x14)
    OP_D2(0x00270444, 0x00270446, 0x15)
    OP_D2(0x00070142, 0x00070146, 0x16)
    OP_D2(0x002701F9, 0x002701FE, 0x17)
    OP_D2(0x002703BC, 0x002703BE, 0x18)
    OP_D2(0x002701FA, 0x002701FF, 0x19)
    OP_D2(0x002703BD, 0x002703BF, 0x1A)

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0004,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0005,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.Eval, "OP_42(0x0A)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_32A',
    )

    OP_D2(0x002700A0, 0x002700A4, 0x1B)
    OP_D2(0x002700A1, 0x002700A5, 0x1C)

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    def _loc_32A(): pass

    label('loc_32A')

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_37C',
    )

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_35E',
    )

    OP_D2(0x00270398, 0x0027039C, 0x1B)
    OP_D2(0x00270399, 0x0027039D, 0x1C)
    OP_A2(0x0003)

    Jump('loc_372')

    def _loc_35E(): pass

    label('loc_35E')

    OP_D2(0x00270398, 0x0027039C, 0x1D)
    OP_D2(0x00270399, 0x0027039D, 0x1E)

    def _loc_372(): pass

    label('loc_372')

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    def _loc_37C(): pass

    label('loc_37C')

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_3F5',
    )

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3B0',
    )

    OP_D2(0x00070020, 0x00070028, 0x1B)
    OP_D2(0x00070021, 0x00070029, 0x1C)
    OP_A2(0x0004)

    Jump('loc_3EB')

    def _loc_3B0(): pass

    label('loc_3B0')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3D7',
    )

    OP_D2(0x00070020, 0x00070028, 0x1D)
    OP_D2(0x00070021, 0x00070029, 0x1E)
    OP_A2(0x0005)

    Jump('loc_3EB')

    def _loc_3D7(): pass

    label('loc_3D7')

    OP_D2(0x00070020, 0x00070028, 0x1F)
    OP_D2(0x00070021, 0x00070029, 0x20)

    def _loc_3EB(): pass

    label('loc_3EB')

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    def _loc_3F5(): pass

    label('loc_3F5')

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_468',
    )

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_426',
    )

    OP_D2(0x00070030, 0x00070038, 0x1D)
    OP_D2(0x00070031, 0x00070039, 0x1E)

    Jump('loc_45E')

    def _loc_426(): pass

    label('loc_426')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_44A',
    )

    OP_D2(0x00070030, 0x00070038, 0x1F)
    OP_D2(0x00070031, 0x00070039, 0x20)

    Jump('loc_45E')

    def _loc_44A(): pass

    label('loc_44A')

    OP_D2(0x00070030, 0x00070038, 0x21)
    OP_D2(0x00070031, 0x00070039, 0x22)

    def _loc_45E(): pass

    label('loc_45E')

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    def _loc_468(): pass

    label('loc_468')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_4DB',
    )

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_499',
    )

    OP_D2(0x00070050, 0x00070058, 0x1F)
    OP_D2(0x00070051, 0x00070059, 0x20)

    Jump('loc_4D1')

    def _loc_499(): pass

    label('loc_499')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4BD',
    )

    OP_D2(0x00070050, 0x00070058, 0x21)
    OP_D2(0x00070051, 0x00070059, 0x22)

    Jump('loc_4D1')

    def _loc_4BD(): pass

    label('loc_4BD')

    OP_D2(0x00070050, 0x00070058, 0x23)
    OP_D2(0x00070051, 0x00070059, 0x24)

    def _loc_4D1(): pass

    label('loc_4D1')

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    def _loc_4DB(): pass

    label('loc_4DB')

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_56C',
    )

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_516',
    )

    OP_D2(0x00070060, 0x00070068, 0x21)
    OP_D2(0x00070061, 0x00070069, 0x22)

    ExecExpressionWithReg(
        0x0004,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_562')

    def _loc_516(): pass

    label('loc_516')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_544',
    )

    OP_D2(0x00070060, 0x00070068, 0x23)
    OP_D2(0x00070061, 0x00070069, 0x24)

    ExecExpressionWithReg(
        0x0004,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_562')

    def _loc_544(): pass

    label('loc_544')

    OP_D2(0x00070060, 0x00070068, 0x25)
    OP_D2(0x00070061, 0x00070069, 0x26)

    ExecExpressionWithReg(
        0x0004,
        (
            (Expr.PushLong, 0x3),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_562(): pass

    label('loc_562')

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    def _loc_56C(): pass

    label('loc_56C')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_5CF',
    )

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_5A7',
    )

    OP_D2(0x00070070, 0x00070078, 0x23)
    OP_D2(0x00070071, 0x00070079, 0x24)

    ExecExpressionWithReg(
        0x0005,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_5C5')

    def _loc_5A7(): pass

    label('loc_5A7')

    OP_D2(0x00070070, 0x00070078, 0x25)
    OP_D2(0x00070071, 0x00070079, 0x26)

    ExecExpressionWithReg(
        0x0005,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_5C5(): pass

    label('loc_5C5')

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    def _loc_5CF(): pass

    label('loc_5CF')

    SetChrChipByIndex(0x0011, 28)
    SetChrChipByIndex(0x0012, 30)
    SetChrChipByIndex(0x0013, 32)
    SetChrChipByIndex(0x0014, 34)
    SetChrChipByIndex(0x0015, 36)
    SetChrChipByIndex(0x0016, 38)
    SetChrChipByIndex(0x0008, 15)
    SetChrSubChip(0x0008, 2)
    SetChrPos(0x0008, 7430, 2590, 0, 270)
    SetChrFlags(0x0008, 0x0800)
    ClearChrFlags(0x0008, 0x0080)
    SetChrPos(0x0009, -8090, 200, 12500, 315)
    ClearChrFlags(0x0009, 0x0080)
    SetChrFlags(0x0009, 0x0800)
    SetChrFlags(0x0009, 0x0002)
    SetChrSubChip(0x0009, 7)
    SetChrChipByIndex(0x0009, 0)
    OP_72(0x0001, 0x0004)
    OP_A1(0x0020, 0x0001)
    SetChrPos(0x0020, -3000, 200, 10000, 145)
    OP_6F(0x0001, 1150)
    OP_70(0x0001, 0x0000047E)
    OP_82(0x80, 0x00)
    OP_82(0x81, 0x00)
    OP_82(0x88, 0x00)
    SetChrChipByIndex(0x0101, 3)
    SetChrChipByIndex(0x0102, 6)
    SetChrChipByIndex(0x00F8, 11)
    SetChrChipByIndex(0x00F9, 13)
    SetChrSubChip(0x0000, 0)
    SetChrSubChip(0x0001, 0)
    SetChrSubChip(0x0002, 0)
    SetChrSubChip(0x0003, 0)
    SetChrPos(0x0101, -240, 3130, -560, 90)
    SetChrPos(0x0102, 230, 3040, 550, 90)
    SetChrPos(0x00F8, -1310, 3200, -1020, 90)
    SetChrPos(0x00F9, -1350, 3200, 1030, 90)
    OP_6D(-9600, 10910, -80, 0)
    OP_67(0, 5020, -10000, 0)
    OP_6B(3250, 0)
    OP_6C(90000, 0)
    OP_6E(516, 0)
    OP_79(0x12, 0x0002)
    OP_79(0x13, 0x0002)
    OP_79(0x14, 0x0002)
    OP_7B()
    FadeIn(2000, 0)
    OP_0D()
    Sleep(500)

    Fade(500)
    OP_6D(5750, 2580, 0, 0)
    OP_67(0, 4490, -10000, 0)
    OP_6B(2370, 0)
    OP_6C(90000, 0)
    OP_6E(446, 0)
    ClearChrFlags(0x0009, 0x0800)
    SetChrSubChip(0x0009, 0)
    SetChrChipByIndex(0x0009, 17)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0150420775V#1156F怎……怎会的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150420776V『辉之环』……\n',
            '消…消…消失了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150420777V#1157F不可能……\n',
            '不可能！！怎么会这样啊！！！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    LoadEffect(0x00, 'battle\\\\mgaria0.eff')
    LoadEffect(0x01, 'map\\\\mp049_22.eff')

    @scena.Lambda('lambda_084E')
    def lambda_084E():
        OP_6D(7750, 2580, 0, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_084E)

    @scena.Lambda('lambda_0866')
    def lambda_0866():
        OP_6B(2600, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0866)

    @scena.Lambda('lambda_0876')
    def lambda_0876():
        OP_9E(0x00FE, 0x0000001E, 0x00000000, 0x00001388, 0x000007D0)
        Yield()

        Jump('lambda_0876')

    DispatchAsync2(0x0008, 0x0000, lambda_0876)

    Sleep(300)

    OP_99(0x0008, 0x02, 0x00, 0x000003E8)
    TerminateThread(0x0008, 0x00)
    Fade(250)
    OP_22(0x00D5, 0x00, 0x64)
    SetChrChipByIndex(0x0008, 16)
    SetChrSubChip(0x0008, 0)
    PlayEffect(0x00, 0x00, 0x0008, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_0D()
    Sleep(500)

    OP_99(0x0008, 0x00, 0x04, 0x000007D0)
    OP_22(0x00D8, 0x00, 0x64)
    OP_99(0x0008, 0x05, 0x09, 0x000007D0)
    OP_82(0x00, 0x02)
    Sleep(300)

    OP_22(0x0099, 0x00, 0x64)
    OP_22(0x00B8, 0x00, 0x64)
    PlayEffect(0x01, 0x01, 0x0008, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)

    @scena.Lambda('lambda_0952')
    def lambda_0952():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x000001F4)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0952)

    WaitForThreadExit(0x0008, 0x0001)
    OP_83(0x01, 0x02)
    OP_82(0x00, 0x02)
    SetChrFlags(0x0008, 0x0080)
    Sleep(1000)

    If(
        (
            (Expr.Eval, "OP_42(0x08)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_9A2',
    )

    ChrTalk(
        0x0109,
        (
            '#0180420778V#1063F！！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B27')

    def _loc_9A2(): pass

    label('loc_9A2')

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_9D2',
    )

    ChrTalk(
        0x0107,
        (
            '#0070321454V#065F啊……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B27')

    def _loc_9D2(): pass

    label('loc_9D2')

    If(
        (
            (Expr.Eval, "OP_42(0x0E)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_A02',
    )

    ChrTalk(
        0x010F,
        (
            '#0100420780V#173F啊……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B27')

    def _loc_A02(): pass

    label('loc_A02')

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_A33',
    )

    ChrTalk(
        0x0105,
        (
            '#0060420781V#1162F啊……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B27')

    def _loc_A33(): pass

    label('loc_A33')

    If(
        (
            (Expr.Eval, "OP_42(0x0A)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_A63',
    )

    ChrTalk(
        0x010B,
        (
            '#0090420782V#213F啊……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B27')

    def _loc_A63(): pass

    label('loc_A63')

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_A91',
    )

    ChrTalk(
        0x0104,
        (
            '#0040420783V#032F！！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B27')

    def _loc_A91(): pass

    label('loc_A91')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_ABF',
    )

    ChrTalk(
        0x0108,
        (
            '#0080420784V#072F！！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B27')

    def _loc_ABF(): pass

    label('loc_ABF')

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_AEF',
    )

    ChrTalk(
        0x0103,
        (
            '#0030420785V#022F啊……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B27')

    def _loc_AEF(): pass

    label('loc_AEF')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_B27',
    )

    ChrTalk(
        0x0106,
        (
            '#0050420786V#054F<FIXME>ヤロォ……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_B27(): pass

    label('loc_B27')

    If(
        (
            (Expr.Eval, "OP_42(0x0F)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_B66',
    )

    ChrTalk(
        0x0110,
        (
            '#0110420787V#276F<FIXME>逃げられたか……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_D21')

    def _loc_B66(): pass

    label('loc_B66')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_B9C',
    )

    ChrTalk(
        0x0106,
        (
            '#0050420788V#054F他逃跑了……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_D21')

    def _loc_B9C(): pass

    label('loc_B9C')

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_BD2',
    )

    ChrTalk(
        0x0103,
        (
            '#0030420789V#024F逃走了啊……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_D21')

    def _loc_BD2(): pass

    label('loc_BD2')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_C06',
    )

    ChrTalk(
        0x0108,
        (
            '#0080420790V#076F逃了吗……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_D21')

    def _loc_C06(): pass

    label('loc_C06')

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_C3C',
    )

    ChrTalk(
        0x0104,
        (
            '#0040420791V#032F逃走了吗……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_D21')

    def _loc_C3C(): pass

    label('loc_C3C')

    If(
        (
            (Expr.Eval, "OP_42(0x0A)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_C6E',
    )

    ChrTalk(
        0x010B,
        (
            '#0090420792V#216F逃、逃了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_D21')

    def _loc_C6E(): pass

    label('loc_C6E')

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_CA7',
    )

    ChrTalk(
        0x0105,
        (
            '#0060420793V#1163F逃、逃走了……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_D21')

    def _loc_CA7(): pass

    label('loc_CA7')

    If(
        (
            (Expr.Eval, "OP_42(0x0E)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_CEA',
    )

    ChrTalk(
        0x010F,
        (
            '#0100420794V#175F<FIXME>に、逃げられたか……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_D21')

    def _loc_CEA(): pass

    label('loc_CEA')

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_D21',
    )

    ChrTalk(
        0x0107,
        (
            '#0070420795V#065F被、被他逃走了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_D21(): pass

    label('loc_D21')

    ChrTalk(
        0x0101,
        (
            '#0010420796V#1022F#5P那种家伙\n',
            '就不要去管他了！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010420797V#1020F现在重要的是……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(250)
    OP_22(0x00D5, 0x00, 0x64)
    SetChrChipByIndex(0x0101, 65535)
    SetChrChipByIndex(0x0102, 65535)
    SetChrChipByIndex(0x00F8, 65535)
    SetChrChipByIndex(0x00F9, 65535)
    WaitForThreadExit(0x0101, 0x0000)
    Sleep(500)

    Fade(500)
    OP_6D(-4450, 3150, 1350, 0)
    OP_67(0, 4490, -10000, 0)
    OP_6B(2370, 0)
    OP_6C(20000, 0)
    OP_6E(446, 0)
    SetChrPos(0x0102, -540, 3200, 40, 90)

    @scena.Lambda('lambda_0E01')
    def lambda_0E01():
        ChrTurnDirection(0x00FE, 0x0009, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_0E01)

    Sleep(50)

    @scena.Lambda('lambda_0E14')
    def lambda_0E14():
        ChrTurnDirection(0x00FE, 0x0009, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0E14)

    Sleep(50)

    @scena.Lambda('lambda_0E27')
    def lambda_0E27():
        ChrTurnDirection(0x00FE, 0x0009, 400)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_0E27)

    Sleep(50)

    ChrTurnDirection(0x00F8, 0x0009, 400)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0102,
        (
            '#0020420798V#1046F#6P#3S莱维！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0x00000000, 0x000000C8, 0x00000BB8, 0x00000064)
    CloseMessageWindow()
    CreateThread(0x0102, 0x01, 0x01, 0x0004)
    Sleep(500)

    CreateThread(0x0101, 0x01, 0x01, 0x0005)

    If(
        (
            (Expr.Eval, "OP_42(0x08)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_F03',
    )

    Sleep(800)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_EB3',
    )

    CreateThread(0x00F9, 0x01, 0x01, 0x0007)

    Jump('loc_EBA')

    def _loc_EB3(): pass

    label('loc_EB3')

    CreateThread(0x00F8, 0x01, 0x01, 0x0006)

    def _loc_EBA(): pass

    label('loc_EBA')

    Sleep(1000)

    ChrTalk(
        0x0109,
        (
            '#0180420799V#1063F#6P…………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CreateThread(0x0109, 0x01, 0x01, 0x0008)
    Sleep(1500)

    Jump('loc_F20')

    def _loc_F03(): pass

    label('loc_F03')

    Sleep(800)

    CreateThread(0x00F9, 0x01, 0x01, 0x0007)
    Sleep(400)

    CreateThread(0x00F8, 0x01, 0x01, 0x0006)
    Sleep(1000)

    def _loc_F20(): pass

    label('loc_F20')

    Fade(500)
    OP_6D(-8550, 200, 12720, 0)
    OP_67(0, 5220, -10000, 0)
    OP_6B(2700, 0)
    OP_6C(20000, 0)
    OP_6E(334, 0)
    OP_0D()
    WaitForThreadExit(0x0102, 0x0001)
    Sleep(500)

    ChrTalk(
        0x0102,
        (
            '#0020420800V#1046F#6P莱维……振作一点啊！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020420801V我现在……马上就给你包扎伤口！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    WaitForThreadExit(0x0101, 0x0001)
    Sleep(100)

    OP_1D(0x72)
    Sleep(500)

    ExecExpressionWithValue(
        0x0009,
        0x08,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(300)

    ExecExpressionWithValue(
        0x0009,
        0x08,
        (
            (Expr.PushLong, 0x3),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(300)

    ExecExpressionWithValue(
        0x0009,
        0x08,
        (
            (Expr.PushLong, 0x5),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(300)

    @scena.Lambda('lambda_100F')
    def lambda_100F():
        OP_6B(2200, 50000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_100F)

    Sleep(500)

    ChrTalk(
        0x0009,
        (
            '#0140420802V#121F#5P#40W……没那个必要了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140420803V#40W你应该……看得出来才对……\n',
            '……我的伤已经没救了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020420804V#1059F#6P不要！！……我不要啊！！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020420805V连莱维也……\n',
            '……和姐姐一样……！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020420806V怎么可以……\n',
            '……为什么会变成这样啊！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0140420807V#121F#5P#40W呵呵……别摆出那种哭丧脸……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140420808V#40W……怎么又变得和小时候一样了……\n',
            '……像个软弱的爱哭鬼。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020420809V#1059F#6P没错！！\n',
            '我就是软弱……我就是没用的爱哭鬼……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020420810V我还需要……\n',
            '……还需要莱维……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020420811V所以……求求你……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ExecExpressionWithValue(
        0x0009,
        0x08,
        (
            (Expr.PushLong, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(200)

    Sleep(500)

    ChrTalk(
        0x0009,
        (
            '#0140420812V#124F#5P#40W……哎呀呀……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140420813V#40W告诉你……约修亚……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140420814V#40W……如果想守护自己珍惜的事物……\n',
            '就一定要活下去，不能死……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140420815V#40W千万不要像……\n',
            '我和你姐姐一样……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140420816V#40W……一定要……努力活下去……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020420817V#1044F#6P！！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ExecExpressionWithValue(
        0x0009,
        0x08,
        (
            (Expr.PushLong, 0x5),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(200)

    Sleep(500)

    ChrTalk(
        0x0009,
        (
            '#0140420818V#121F#5P#40W艾丝蒂尔·布莱特………\n',
            '…………我……有个请求………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010420819V#1025F#6P嗯……是什么呢……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0140420820V#121F#5P#40W这个傻瓜虽然表面看来很坚强……\n',
            '……但他的内心……也有着脆弱的一面，',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140420821V#40W如今一切束缚都已经解除……\n',
            '……是时候……\n',
            '#40W让他真正学着坚强了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140420822V#124F#40W……所以，拜托你……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140420823V#40W今后也请继续……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140420824V#40W支撑着他……支撑着\n',
            '……我的弟弟………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010420825V#1016F#6P哈哈……其实就算你不说\n',
            '我也一定会这么做的………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010420826V#1025F不过……\n',
            '我愿意正式答应你的请求。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010420827V所以……请你安心吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ExecExpressionWithValue(
        0x0009,
        0x08,
        (
            (Expr.PushLong, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(250)

    Sleep(500)

    ChrTalk(
        0x0009,
        (
            '#0140420828V#124F#5P#40W………抱歉…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ExecExpressionWithValue(
        0x0009,
        0x08,
        (
            (Expr.PushLong, 0x5),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(300)

    Sleep(500)

    ChrTalk(
        0x0009,
        (
            '#0140420829V#1431F#5P#40W……呵呵……\n',
            '不过我终于……明白了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140420830V#50W……那个时候……卡琳她……\n',
            '#60W为何……在逝世前会面露微笑了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140420831V#1430F#70W原来躺在亲人身边睡去的感觉…………\n',
            '#80W是这么……舒适………安心啊………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    ExecExpressionWithValue(
        0x0009,
        0x08,
        (
            (Expr.PushLong, 0x7),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(300)

    ExecExpressionWithValue(
        0x0009,
        0x08,
        (
            (Expr.PushLong, 0x8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(300)

    ExecExpressionWithValue(
        0x0009,
        0x08,
        (
            (Expr.PushLong, 0x9),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(400)

    Sleep(1000)

    ChrTalk(
        0x0009,
        (
            '#0140420832V#5P#40W………………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020420833V#1044F#6P莱……莱维……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0140420834V#5P#40W………………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020420835V#1054F#6P别、别开这种玩笑啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020420836V其实你……\n',
            '……听得见的……对吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0140420837V#5P………………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020420838V#1059F#6P你一定能听见的对不对……！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020420839V我们好不容易才能再见面的啊……！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020420840V……我们理应可以……\n',
            '再像从前那样倾心交谈！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0140420841V#5P………………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020420842V#1057F#6P求求你……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(
        0x0102,
        (
            '#0020420843V#1059F#6P#3S求求你回答我啊！！！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0x00000000, 0x000001F4, 0x00000BB8, 0x00000064)
    CloseMessageWindow()

    ExecExpressionWithValue(
        0x0102,
        0x08,
        (
            (Expr.PushLong, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(200)

    ExecExpressionWithValue(
        0x0102,
        0x08,
        (
            (Expr.PushLong, 0x5),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(300)

    @scena.Lambda('lambda_1A03')
    def lambda_1A03():
        OP_9E(0x00FE, 0x0000000A, 0x00000000, 0x0000012C, 0x000007D0)
        Yield()

        Jump('lambda_1A03')

    DispatchAsync2(0x0102, 0x0003, lambda_1A03)

    ChrTalk(
        0x0101,
        (
            '#0010420844V#1026F#6P约修亚……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x0A)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1A77',
    )

    ChrTalk(
        0x010B,
        (
            '#0090420845V#417F#6P………呜…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1A77(): pass

    label('loc_1A77')

    If(
        (
            (Expr.Eval, "OP_42(0x0E)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1AB7',
    )

    ChrTalk(
        0x010F,
        (
            '#0100420846V#175F<FIXME>………女神よ…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1AB7(): pass

    label('loc_1AB7')

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1AEA',
    )

    ChrTalk(
        0x0105,
        (
            '#0060420847V#1169F#6P约修亚……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1AEA(): pass

    label('loc_1AEA')

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1B20',
    )

    ChrTalk(
        0x0107,
        (
            '#0070420848V#562F#6P大…大哥哥……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1B20(): pass

    label('loc_1B20')

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1B5A',
    )

    ChrTalk(
        0x0103,
        (
            '#0030420849V#522F#6P……约修亚…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1B5A(): pass

    label('loc_1B5A')

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1B94',
    )

    ChrTalk(
        0x0104,
        (
            '#0040420850V#032F#6P……约修亚…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1B94(): pass

    label('loc_1B94')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1BE9',
    )

    ChrTalk(
        0x0106,
        (
            '#0050420851V#552F#6P才赢了一次就逃跑……\n',
            '可恶……你也太狡猾了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1BE9(): pass

    label('loc_1BE9')

    If(
        (
            (Expr.Eval, "OP_42(0x0F)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1C26',
    )

    ChrTalk(
        0x0110,
        (
            '#0110420852V#276F………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1C26(): pass

    label('loc_1C26')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1C66',
    )

    ChrTalk(
        0x0108,
        (
            '#0080420853V#572F#6P………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1C66(): pass

    label('loc_1C66')

    TerminateThread(0x0102, 0x03)
    SetChrChipByIndex(0x000B, 19)
    SetChrChipByIndex(0x000A, 21)
    SetChrChipByIndex(0x000C, 22)
    SetChrChipByIndex(0x000D, 24)
    SetChrChipByIndex(0x000E, 26)

    If(
        (
            (Expr.Eval, "OP_42(0x0E)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1CCF',
    )

    SetChrPos(0x000B, -18830, 250, -1230, 45)

    NpcTalk(
        0x000B,
        '女性的声音',
        (
            '#0100420854V#2P喂～～！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1D76')

    def _loc_1CCF(): pass

    label('loc_1CCF')

    If(
        (
            (Expr.Eval, "OP_42(0x0F)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1D26',
    )

    SetChrPos(0x000B, -18830, 250, -1230, 45)

    NpcTalk(
        0x000B,
        '男の声',
        (
            '#0100420855V#2P<FIXME>──ここにいたか！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1D76')

    def _loc_1D26(): pass

    label('loc_1D26')

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1D76',
    )

    SetChrPos(0x000B, -18830, 250, -1230, 45)

    NpcTalk(
        0x000B,
        '娘の声',
        (
            '#0100420856V#2P<FIXME>……皆さん！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1D76(): pass

    label('loc_1D76')

    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(50)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1DB9',
    )

    OP_62(0x00F8, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    Jump('loc_1DF7')

    def _loc_1DB9(): pass

    label('loc_1DB9')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1DE0',
    )

    OP_62(0x00F8, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    Jump('loc_1DF7')

    def _loc_1DE0(): pass

    label('loc_1DE0')

    OP_62(0x00F8, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    def _loc_1DF7(): pass

    label('loc_1DF7')

    Sleep(50)

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1E23',
    )

    OP_62(0x00F9, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    Jump('loc_1E61')

    def _loc_1E23(): pass

    label('loc_1E23')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1E4A',
    )

    OP_62(0x00F9, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    Jump('loc_1E61')

    def _loc_1E4A(): pass

    label('loc_1E4A')

    OP_62(0x00F9, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    def _loc_1E61(): pass

    label('loc_1E61')

    Sleep(1000)

    @scena.Lambda('lambda_1E6C')
    def lambda_1E6C():
        OP_6D(-9880, 200, 9120, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1E6C)

    @scena.Lambda('lambda_1E84')
    def lambda_1E84():
        OP_67(0, 4580, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_1E84)

    @scena.Lambda('lambda_1E9C')
    def lambda_1E9C():
        OP_6B(2700, 3000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_1E9C)

    @scena.Lambda('lambda_1EAC')
    def lambda_1EAC():
        OP_6E(392, 3000)

        ExitThread()

    DispatchAsync(0x0102, 0x0003, lambda_1EAC)

    @scena.Lambda('lambda_1EBC')
    def lambda_1EBC():
        OP_8C(0x00FE, 225, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1EBC)

    Sleep(100)

    @scena.Lambda('lambda_1ECF')
    def lambda_1ECF():
        OP_8C(0x00FE, 225, 400)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_1ECF)

    Sleep(100)

    @scena.Lambda('lambda_1EE2')
    def lambda_1EE2():
        OP_8C(0x00FE, 225, 400)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_1EE2)

    If(
        (
            (Expr.Eval, "OP_42(0x0E)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1EFF',
    )

    CreateThread(0x000B, 0x01, 0x01, 0x0012)

    def _loc_1EFF(): pass

    label('loc_1EFF')

    Sleep(600)

    If(
        (
            (Expr.Eval, "OP_42(0x0F)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1F19',
    )

    CreateThread(0x000A, 0x01, 0x01, 0x0013)

    def _loc_1F19(): pass

    label('loc_1F19')

    Sleep(350)

    CreateThread(0x0012, 0x01, 0x01, 0x0015)
    Sleep(230)

    CreateThread(0x0011, 0x01, 0x01, 0x0014)
    Sleep(280)

    CreateThread(0x0013, 0x01, 0x01, 0x0016)
    Sleep(230)

    CreateThread(0x0014, 0x01, 0x01, 0x0017)
    Sleep(250)

    CreateThread(0x0015, 0x01, 0x01, 0x0018)
    Sleep(200)

    If(
        (
            (Expr.Eval, "OP_42(0x08)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1F6F',
    )

    CreateThread(0x0016, 0x01, 0x01, 0x0019)

    def _loc_1F6F(): pass

    label('loc_1F6F')

    Sleep(600)

    CreateThread(0x000C, 0x01, 0x01, 0x001A)
    Sleep(250)

    CreateThread(0x000E, 0x01, 0x01, 0x001B)
    Sleep(200)

    CreateThread(0x000D, 0x01, 0x01, 0x001C)
    WaitForThreadExit(0x0012, 0x0001)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_1FB3',
    )

    SetChrPos(0x0017, -11990, 200, 6140, 0)

    Jump('loc_1FC4')

    def _loc_1FB3(): pass

    label('loc_1FB3')

    SetChrPos(0x0017, -11310, 200, 5080, 0)

    def _loc_1FC4(): pass

    label('loc_1FC4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_1FDF',
    )

    SetChrPos(0x0018, -11990, 200, 6140, 0)

    Jump('loc_200B')

    def _loc_1FDF(): pass

    label('loc_1FDF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_1FFA',
    )

    SetChrPos(0x0018, -11310, 200, 5080, 0)

    Jump('loc_200B')

    def _loc_1FFA(): pass

    label('loc_1FFA')

    SetChrPos(0x0018, -12640, 200, 7450, 0)

    def _loc_200B(): pass

    label('loc_200B')

    ChrTalk(
        0x0101,
        (
            '#0010420857V#1004F#5P啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x0E)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2573',
    )

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2157',
    )

    ChrTalk(
        0x0105,
        (
            '#0060420858V#1163F#2P尤莉亚小姐……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0100420859V#170F#6P太好了……看来大家都平安无事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000B, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    OP_8C(0x000B, 0, 400)
    Sleep(500)

    ChrTalk(
        0x000B,
        (
            '#0100420860V#173F#6P……啊……他……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060420861V#1169F#2P……………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0100420862V#175F#6P是吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2346')

    def _loc_2157(): pass

    label('loc_2157')

    If(
        (
            (Expr.Eval, "OP_42(0x0F)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_226B',
    )

    ChrTalk(
        0x0110,
        (
            '#0110420863V#270F<FIXME>大尉か……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0100420859V#170F#6P太好了……大家都没事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000B, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    OP_8C(0x000B, 0, 400)
    Sleep(500)

    ChrTalk(
        0x000B,
        (
            '#0100420860V#173F#6P……啊……他……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010420866V#1003F#5P……………嗯…………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0100420867V#175F#6P是吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2346')

    def _loc_226B(): pass

    label('loc_226B')

    ChrTalk(
        0x000B,
        (
            '#0100420868V#170F#6P太好了……大家都没事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000B, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    OP_8C(0x000B, 0, 400)
    Sleep(500)

    ChrTalk(
        0x000B,
        (
            '#0100420860V#173F#6P……啊……他……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010420870V#1003F#5P……………嗯…………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0100420867V#175F#6P是吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2346(): pass

    label('loc_2346')

    If(
        (
            (Expr.Eval, "OP_42(0x0F)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_23F1',
    )

    ChrTalk(
        0x000A,
        (
            '#0110420872V#272F#6P……你们搭升降梯下去之后，\n',
            '又出现了好几只机械龙……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0110420873V#270F就在大家陷入绝境的时候，\n',
            '是他驾驶着那部机械龙\n',
            '将战局扭转。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2570')

    def _loc_23F1(): pass

    label('loc_23F1')

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_24C0',
    )

    ChrTalk(
        0x0017,
        (
            '#0060420874V#1167F<FIXME>……皆さんが降りた後、\n',
            '新手の機械獣が何匹も現れて……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060420875V#1162F絶体絶命に陥った時、\n',
            'レーヴェさんがそこの機械竜を\n',
            '呼んで戦況を覆してくださったんです。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2570')

    def _loc_24C0(): pass

    label('loc_24C0')

    ChrTalk(
        0x0018,
        (
            '#0030420876V#026F<FIXME>……あんたたちが降りた後、\n',
            '新手の機械獣が何匹も現れて……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030420877V#022F絶体絶命に陥った時、\n',
            '彼がそこの機械竜を呼んで\n',
            '戦況を覆してくれたのよ。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2570(): pass

    label('loc_2570')

    Jump('loc_2A00')

    def _loc_2573(): pass

    label('loc_2573')

    If(
        (
            (Expr.Eval, "OP_42(0x0F)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2802',
    )

    ChrTalk(
        0x010F,
        (
            '#0100420878V#173F<FIXME>……少佐………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0110420879V#270F<FIXME>……全員無事か。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000A, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x000A,
        (
            '#0110420880V#273F<FIXME>ひょっとして彼は……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010420881V#1003F#5P……………嗯…………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0110420882V#276F#6P是吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_274F',
    )

    ChrTalk(
        0x0017,
        (
            '#0060420874V#1167F<FIXME>……皆さんが降りた後、\n',
            '新手の機械獣が何匹も現れて……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060420875V#1162F絶体絶命に陥った時、\n',
            'レーヴェさんがそこの機械竜を\n',
            '呼んで戦況を覆してくださったんです。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_27FF')

    def _loc_274F(): pass

    label('loc_274F')

    ChrTalk(
        0x0018,
        (
            '#0030420876V#026F<FIXME>……あんたたちが降りた後、\n',
            '新手の機械獣が何匹も現れて……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030420877V#022F絶体絶命に陥った時、\n',
            '彼がそこの機械竜を呼んで\n',
            '戦況を覆してくれたのよ。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_27FF(): pass

    label('loc_27FF')

    Jump('loc_2A00')

    def _loc_2802(): pass

    label('loc_2802')

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2A00',
    )

    ChrTalk(
        0x0101,
        (
            '#0010420887V#1025F<FIXME>みんな……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0017,
        (
            '#0060420888V#1162F<FIXME>皆さん、ご無事ですか！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0017, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_289D',
    )

    OP_8C(0x0011, 0, 400)

    Jump('loc_28A4')

    def _loc_289D(): pass

    label('loc_289D')

    OP_8C(0x0012, 0, 400)

    def _loc_28A4(): pass

    label('loc_28A4')

    Sleep(500)

    ChrTalk(
        0x0017,
        (
            '#0060420889V#1164F<FIXME>……あ…………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060420890V#1163Fエステルさん……\n',
            '……あの、もしかして………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010420891V#1003F<FIXME>……………うん…………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0018,
        (
            '#0030420876V#026F<FIXME>……あんたたちが降りた後、\n',
            '新手の機械獣が何匹も現れて……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030420877V#022F絶体絶命に陥った時、\n',
            '彼がそこの機械竜を呼んで\n',
            '戦況を覆してくれたのよ。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2A00(): pass

    label('loc_2A00')

    ChrTalk(
        0x0101,
        (
            '#0010420894V#1025F#5P原来是这样……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0540420895V#102F#6P……那怀斯曼和\n',
            '『辉之环』怎么样了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010420896V#1015F#5P啊……嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010420897V#1007F『辉之环』\n',
            '不知为何消失了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010420898V怀斯曼也逃跑了……\n',
            '看起来似乎非常慌张。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0540420899V#103F#6P什么……消失了？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540420900V#104F嗯嗯……\n',
            '这下或许糟糕了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010210711V#1004F#5P哎……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CreateThread(0x0009, 0x03, 0x01, 0x0003)
    OP_22(0x0085, 0x01, 0x50)
    Sleep(1000)

    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010420902V#1020F#5P这、这摇晃是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0540420903V#104F#6P……『辉之环』是这座\n',
            '浮游都市的核心能源。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540420904V#102F如果它消失的话……\n',
            '这座城市也就要随之崩溃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(50)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2C8A',
    )

    OP_62(0x00F8, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    Jump('loc_2CC8')

    def _loc_2C8A(): pass

    label('loc_2C8A')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2CB1',
    )

    OP_62(0x00F8, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    Jump('loc_2CC8')

    def _loc_2CB1(): pass

    label('loc_2CB1')

    OP_62(0x00F8, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    def _loc_2CC8(): pass

    label('loc_2CC8')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2CEF',
    )

    OP_62(0x00F9, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    Jump('loc_2D2D')

    def _loc_2CEF(): pass

    label('loc_2CEF')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2D16',
    )

    OP_62(0x00F9, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    Jump('loc_2D2D')

    def _loc_2D16(): pass

    label('loc_2D16')

    OP_62(0x00F9, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    def _loc_2D2D(): pass

    label('loc_2D2D')

    Sleep(50)

    OP_62(0x000B, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    OP_62(0x000A, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(50)

    OP_62(0x000D, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    OP_62(0x000E, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0011, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    OP_62(0x0012, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0013, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    If(
        (
            (Expr.PushReg, 0x4),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2E09',
    )

    OP_62(0x0014, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    Jump('loc_2E20')

    def _loc_2E09(): pass

    label('loc_2E09')

    OP_62(0x0014, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    def _loc_2E20(): pass

    label('loc_2E20')

    Sleep(50)

    If(
        (
            (Expr.PushReg, 0x4),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2E4C',
    )

    OP_62(0x0015, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    Jump('loc_2E8A')

    def _loc_2E4C(): pass

    label('loc_2E4C')

    If(
        (
            (Expr.PushReg, 0x5),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2E73',
    )

    OP_62(0x0015, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    Jump('loc_2E8A')

    def _loc_2E73(): pass

    label('loc_2E73')

    OP_62(0x0015, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    def _loc_2E8A(): pass

    label('loc_2E8A')

    If(
        (
            (Expr.Eval, "OP_42(0x08)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2ED6',
    )

    If(
        (
            (Expr.PushReg, 0x4),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2EBF',
    )

    OP_62(0x0016, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    Jump('loc_2ED6')

    def _loc_2EBF(): pass

    label('loc_2EBF')

    OP_62(0x0016, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    def _loc_2ED6(): pass

    label('loc_2ED6')

    Sleep(1000)

    @scena.Lambda('lambda_2EE1')
    def lambda_2EE1():
        ChrTurnDirection(0x00FE, 0x000C, 400)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_2EE1)

    Sleep(50)

    ChrTurnDirection(0x000A, 0x000C, 400)

    If(
        (
            (Expr.Eval, "OP_42(0x0E)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2F39',
    )

    ChrTalk(
        0x010F,
        (
            '#0100420905V#173F#4P<FIXME>そ、それでは……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2F67')

    def _loc_2F39(): pass

    label('loc_2F39')

    ChrTalk(
        0x000B,
        (
            '#0100420905V#173F#5P那、那么说的话……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2F67(): pass

    label('loc_2F67')

    If(
        (
            (Expr.Eval, "OP_42(0x0F)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2FCC',
    )

    ChrTalk(
        0x0110,
        (
            '#0110420907V#272F#4P<FIXME>急いで《アルセイユ》に\n',
            '戻った方がよさそうですな……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3011')

    def _loc_2FCC(): pass

    label('loc_2FCC')

    ChrTalk(
        0x000A,
        (
            '#0110420908V#272F#5P我们必须要马上赶回\n',
            '『埃尔赛尤号』才行啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3011(): pass

    label('loc_3011')

    ChrTalk(
        0x000C,
        (
            '#0540420909V#104F#6P嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540420910V#102F导力应该还不会马上耗尽，\n',
            '抓紧时间的话也许还来得及。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x000C, 180, 400)
    Sleep(300)

    ChrTalk(
        0x000C,
        (
            '#0540420911V#102F#5P你们的飞船现在情况如何了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_30BD')
    def lambda_30BD():
        ChrTurnDirection(0x00FE, 0x000C, 400)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_30BD)

    Sleep(100)

    ChrTurnDirection(0x000E, 0x000C, 400)

    ChrTalk(
        0x000E,
        (
            '#0290420912V#200F#6P啊啊，现在应该已经\n',
            '完全修理好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0300420913V#490F#6P现在回去的话\n',
            '马上就可以起飞。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x0E)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3200',
    )

    @scena.Lambda('lambda_3157')
    def lambda_3157():
        ChrTurnDirection(0x00FE, 0x010F, 400)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_3157)

    @scena.Lambda('lambda_3165')
    def lambda_3165():
        ChrTurnDirection(0x00FE, 0x010F, 400)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_3165)

    Sleep(50)

    @scena.Lambda('lambda_3178')
    def lambda_3178():
        ChrTurnDirection(0x00FE, 0x010F, 400)

        ExitThread()

    DispatchAsync(0x0013, 0x0001, lambda_3178)

    @scena.Lambda('lambda_3186')
    def lambda_3186():
        ChrTurnDirection(0x00FE, 0x010F, 400)

        ExitThread()

    DispatchAsync(0x0014, 0x0001, lambda_3186)

    Sleep(50)

    @scena.Lambda('lambda_3199')
    def lambda_3199():
        ChrTurnDirection(0x00FE, 0x010F, 400)

        ExitThread()

    DispatchAsync(0x0015, 0x0001, lambda_3199)

    @scena.Lambda('lambda_31A7')
    def lambda_31A7():
        ChrTurnDirection(0x00FE, 0x010F, 400)

        ExitThread()

    DispatchAsync(0x0016, 0x0001, lambda_31A7)

    Sleep(50)

    @scena.Lambda('lambda_31BA')
    def lambda_31BA():
        ChrTurnDirection(0x00FE, 0x010F, 400)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_31BA)

    @scena.Lambda('lambda_31C8')
    def lambda_31C8():
        ChrTurnDirection(0x00FE, 0x010F, 400)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_31C8)

    Sleep(50)

    @scena.Lambda('lambda_31DB')
    def lambda_31DB():
        ChrTurnDirection(0x00FE, 0x010F, 400)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_31DB)

    @scena.Lambda('lambda_31E9')
    def lambda_31E9():
        ChrTurnDirection(0x00FE, 0x010F, 400)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_31E9)

    Sleep(50)

    OP_8C(0x000A, 180, 400)

    Jump('loc_32AC')

    def _loc_3200(): pass

    label('loc_3200')

    @scena.Lambda('lambda_3206')
    def lambda_3206():
        ChrTurnDirection(0x00FE, 0x000B, 400)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_3206)

    @scena.Lambda('lambda_3214')
    def lambda_3214():
        ChrTurnDirection(0x00FE, 0x000B, 400)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_3214)

    Sleep(50)

    @scena.Lambda('lambda_3227')
    def lambda_3227():
        ChrTurnDirection(0x00FE, 0x000B, 400)

        ExitThread()

    DispatchAsync(0x0013, 0x0001, lambda_3227)

    @scena.Lambda('lambda_3235')
    def lambda_3235():
        ChrTurnDirection(0x00FE, 0x000B, 400)

        ExitThread()

    DispatchAsync(0x0014, 0x0001, lambda_3235)

    Sleep(50)

    @scena.Lambda('lambda_3248')
    def lambda_3248():
        ChrTurnDirection(0x00FE, 0x000B, 400)

        ExitThread()

    DispatchAsync(0x0015, 0x0001, lambda_3248)

    @scena.Lambda('lambda_3256')
    def lambda_3256():
        ChrTurnDirection(0x00FE, 0x000B, 400)

        ExitThread()

    DispatchAsync(0x0016, 0x0001, lambda_3256)

    Sleep(50)

    @scena.Lambda('lambda_3269')
    def lambda_3269():
        ChrTurnDirection(0x00FE, 0x000B, 400)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_3269)

    @scena.Lambda('lambda_3277')
    def lambda_3277():
        ChrTurnDirection(0x00FE, 0x000B, 400)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_3277)

    Sleep(50)

    @scena.Lambda('lambda_328A')
    def lambda_328A():
        ChrTurnDirection(0x00FE, 0x000B, 400)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_328A)

    @scena.Lambda('lambda_3298')
    def lambda_3298():
        ChrTurnDirection(0x00FE, 0x000B, 400)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_3298)

    Sleep(50)

    OP_8C(0x000A, 180, 400)

    def _loc_32AC(): pass

    label('loc_32AC')

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            (Expr.Eval, "OP_42(0x0F)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_335F',
    )

    ChrTalk(
        0x000B,
        (
            '#0100420914V#177F#5P很好……那么各位，\n',
            '我们现在就开始撤退！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100420915V在升降梯附近就有\n',
            '传送门！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100420916V大家依次搭乘那个\n',
            '离开『中枢塔』！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_35B9')

    def _loc_335F(): pass

    label('loc_335F')

    If(
        (
            (Expr.Eval, "OP_42(0x0F)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3491',
    )

    If(
        (
            (Expr.Eval, "OP_42(0x0E)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_33C9',
    )

    ChrTalk(
        0x010F,
        (
            '#0100420917V#177F<FIXME>よし……それでは皆、\n',
            'これより撤退を開始する！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_340A')

    def _loc_33C9(): pass

    label('loc_33C9')

    ChrTalk(
        0x000B,
        (
            '#0100420917V#177F#5P很好……那么各位，\n',
            '我们现在就开始撤退！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_340A(): pass

    label('loc_340A')

    ChrTalk(
        0x000A,
        (
            '#0110420919V#271F<FIXME>エレベーター近くに\n',
            '転位用のゲートがあった。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0110420920V順次、それを使って\n',
            '《中枢塔》より脱出するぞ！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_35B9')

    def _loc_3491(): pass

    label('loc_3491')

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_35B9',
    )

    If(
        (
            (Expr.Eval, "OP_42(0x0E)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_34F1',
    )

    ChrTalk(
        0x010F,
        (
            '#0100420917V#177F#5P很好……那么各位，\n',
            '我们现在就开始撤退！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3532')

    def _loc_34F1(): pass

    label('loc_34F1')

    ChrTalk(
        0x000B,
        (
            '#0100420917V#177F#5P很好……那么各位，\n',
            '我们现在就开始撤退！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3532(): pass

    label('loc_3532')

    ChrTalk(
        0x0017,
        (
            '#0060420923V#1162F<FIXME>エレベーター近くに\n',
            '転位用のゲートがありました。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060420924Vそれを使って\n',
            '《中枢塔》より脱出しましょう！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_35B9(): pass

    label('loc_35B9')

    Sleep(300)

    @scena.Lambda('lambda_35C4')
    def lambda_35C4():
        OP_6D(-20380, 200, 3160, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_35C4)

    @scena.Lambda('lambda_35DC')
    def lambda_35DC():
        OP_67(0, 5690, -10000, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_35DC)

    @scena.Lambda('lambda_35F4')
    def lambda_35F4():
        OP_6B(3390, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_35F4)

    @scena.Lambda('lambda_3604')
    def lambda_3604():
        OP_6C(45000, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_3604)

    @scena.Lambda('lambda_3614')
    def lambda_3614():
        OP_6E(456, 6000)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_3614)

    Sleep(300)

    CreateThread(0x000D, 0x00, 0x01, 0x0027)
    Sleep(200)

    CreateThread(0x000E, 0x00, 0x01, 0x0026)
    Sleep(200)

    CreateThread(0x000C, 0x00, 0x01, 0x0025)
    Sleep(400)

    CreateThread(0x0016, 0x00, 0x01, 0x0024)
    Sleep(100)

    CreateThread(0x0015, 0x00, 0x01, 0x0023)
    Sleep(150)

    CreateThread(0x0014, 0x00, 0x01, 0x0022)
    Sleep(180)

    CreateThread(0x0012, 0x00, 0x01, 0x0020)
    Sleep(200)

    CreateThread(0x0013, 0x00, 0x01, 0x0021)
    Sleep(250)

    CreateThread(0x0011, 0x00, 0x01, 0x001F)
    Sleep(250)

    If(
        (
            (Expr.Eval, "OP_42(0x0E)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_36A4',
    )

    CreateThread(0x000B, 0x00, 0x01, 0x001D)

    def _loc_36A4(): pass

    label('loc_36A4')

    Sleep(350)

    If(
        (
            (Expr.Eval, "OP_42(0x0F)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_36BE',
    )

    CreateThread(0x000A, 0x00, 0x01, 0x001E)

    def _loc_36BE(): pass

    label('loc_36BE')

    Sleep(100)

    CreateThread(0x00F8, 0x00, 0x01, 0x0028)
    Sleep(300)

    CreateThread(0x00F9, 0x00, 0x01, 0x0029)
    WaitForThreadExit(0x0101, 0x0000)
    Sleep(2000)

    Fade(1000)
    OP_6D(-8029, 200, 11880, 0)
    OP_67(0, 5760, -10000, 0)
    OP_6B(1960, 0)
    OP_6C(21000, 0)
    OP_6E(411, 0)
    OP_0D()
    Sleep(500)

    OP_8C(0x0101, 315, 400)
    Sleep(500)

    ChrTalk(
        0x0102,
        (
            '#0020420925V#1057F#5P…………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010420926V#1027F#6P约修亚……那个……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010420927V我知道你现在很痛苦……不过\n',
            '……要是不快点走的话……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020420928V#1057F#5P对不起……艾丝蒂尔……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020420929V请你……先走吧……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020420930V不用……\n',
            '……不用再管我了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010420931V#1002F#6P…………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_388E')
    def lambda_388E():
        OP_6D(-9030, 200, 13460, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_388E)

    @scena.Lambda('lambda_38A6')
    def lambda_38A6():
        OP_6B(2300, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_38A6)

    OP_8E(0x0101, -9220, 200, 12250, 1500, 0x00)
    WaitForThreadExit(0x0101, 0x0000)
    Fade(250)
    SetChrFlags(0x0101, 0x0080)
    SetChrFlags(0x0102, 0x0800)
    SetChrSubChip(0x0102, 6)
    OP_0D()
    Sleep(500)

    OP_99(0x0102, 0x06, 0x0D, 0x000005DC)
    Sleep(500)

    OP_99(0x0102, 0x0E, 0x0F, 0x000005DC)
    OP_22(0x00A5, 0x00, 0x64)
    OP_99(0x0102, 0x10, 0x1A, 0x000005DC)

    ChrTalk(
        0x0102,
        (
            '#0020331024V#1044F#5P啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ExecExpressionWithValue(
        0x0102,
        0x08,
        (
            (Expr.PushLong, 0x1B),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(150)

    ExecExpressionWithValue(
        0x0102,
        0x08,
        (
            (Expr.PushLong, 0x1C),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(150)

    ExecExpressionWithValue(
        0x0102,
        0x08,
        (
            (Expr.PushLong, 0x1B),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(150)

    ExecExpressionWithValue(
        0x0102,
        0x08,
        (
            (Expr.PushLong, 0x1A),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(300)

    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010420933V#1023F#6P约修亚……马上给我振作起来！！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010420934V莱维刚刚才说过的话\n',
            '你一点也没有听进去吗！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010420935V要想彼此守护，就一定要活下去……\n',
            '难道你这么快就已经忘记了吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020420936V#1042F#5P#3S！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010420937V#1023F#6P我可是不会忘记的！！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010420938V要一直支撑着约修亚，\n',
            '这是我和他之间的约定！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010420939V#1014F#6P#3S我绝对……绝对不会忘记的！！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0x00000000, 0x000001F4, 0x00000BB8, 0x00000064)
    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020420940V#1057F#5P艾丝蒂尔……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020420941V#1035F……对不起……\n',
            '我真的……是个没用的胆小鬼。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(300)

    Fade(250)
    SetChrSubChip(0x0102, 29)
    ClearChrFlags(0x0101, 0x0080)
    ClearChrFlags(0x0102, 0x0002)
    ClearChrFlags(0x0102, 0x0800)
    SetChrChipByIndex(0x0102, 65535)
    SetChrSubChip(0x0102, 0)

    @scena.Lambda('lambda_3B9B')
    def lambda_3B9B():
        OP_8F(0x00FE, -8940, 200, 11910, 800, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_3B9B)

    OP_8C(0x0102, 135, 0)
    OP_0D()
    OP_8C(0x0102, 45, 300)
    Sleep(500)

    SetChrFlags(0x0102, 0x0002)
    SetChrSubChip(0x0102, 0)
    SetChrChipByIndex(0x0102, 2)
    OP_99(0x0102, 0x00, 0x02, 0x000003E8)
    Sleep(500)

    Fade(500)
    OP_22(0x00D5, 0x00, 0x64)
    OP_99(0x0102, 0x03, 0x04, 0x000003E8)
    SetChrSubChip(0x0009, 10)
    OP_0D()
    Sleep(500)

    OP_99(0x0102, 0x05, 0x08, 0x000003E8)
    Sleep(500)

    OP_99(0x0102, 0x08, 0x0B, 0x000005DC)
    Sleep(500)

    OP_99(0x0102, 0x0C, 0x0E, 0x000005DC)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010420942V#1004F#6P啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(500)
    OP_22(0x00D5, 0x00, 0x64)
    SetChrSubChip(0x0102, 17)
    OP_0D()
    Sleep(500)

    OP_99(0x0102, 0x11, 0x13, 0x000003E8)
    Sleep(500)

    ChrTalk(
        0x0102,
        (
            '#0020420943V#1035F#6P莱维……\n',
            '这个……让我替你保管吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020420944V#1041F我会把它带回我们的哈梅尔……\n',
            '交到姐姐的手里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010420945V#1025F#6P……约修亚……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_3D19')
    def lambda_3D19():
        OP_6D(-9140, 200, 12720, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_3D19)

    @scena.Lambda('lambda_3D31')
    def lambda_3D31():
        OP_6B(2600, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_3D31)

    If(
        (
            (Expr.Eval, "OP_42(0x08)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3E3E',
    )

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3DCA',
    )

    If(
        (
            (Expr.Eval, "OP_42(0x0E)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3D6E',
    )

    CreateThread(0x000A, 0x00, 0x01, 0x000B)

    Jump('loc_3D8D')

    def _loc_3D6E(): pass

    label('loc_3D6E')

    If(
        (
            (Expr.Eval, "OP_42(0x0F)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3D86',
    )

    CreateThread(0x000B, 0x00, 0x01, 0x000A)

    Jump('loc_3D8D')

    def _loc_3D86(): pass

    label('loc_3D86')

    CreateThread(0x000B, 0x00, 0x01, 0x000A)

    def _loc_3D8D(): pass

    label('loc_3D8D')

    Sleep(300)

    CreateThread(0x00F9, 0x00, 0x01, 0x0009)

    If(
        (
            (Expr.Eval, "OP_42(0x0E)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3DAF',
    )

    WaitForThreadExit(0x000A, 0x0000)

    Jump('loc_3DC2')

    def _loc_3DAF(): pass

    label('loc_3DAF')

    If(
        (
            (Expr.Eval, "OP_42(0x0F)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3DC2',
    )

    WaitForThreadExit(0x000B, 0x0000)

    def _loc_3DC2(): pass

    label('loc_3DC2')

    WaitForThreadExit(0x00F9, 0x0000)

    Jump('loc_3E3B')

    def _loc_3DCA(): pass

    label('loc_3DCA')

    If(
        (
            (Expr.Eval, "OP_42(0x0E)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3DE2',
    )

    CreateThread(0x000A, 0x00, 0x01, 0x000E)

    Jump('loc_3E01')

    def _loc_3DE2(): pass

    label('loc_3DE2')

    If(
        (
            (Expr.Eval, "OP_42(0x0F)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3DFA',
    )

    CreateThread(0x000B, 0x00, 0x01, 0x000D)

    Jump('loc_3E01')

    def _loc_3DFA(): pass

    label('loc_3DFA')

    CreateThread(0x000B, 0x00, 0x01, 0x000D)

    def _loc_3E01(): pass

    label('loc_3E01')

    Sleep(300)

    CreateThread(0x00F8, 0x00, 0x01, 0x000C)

    If(
        (
            (Expr.Eval, "OP_42(0x0E)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3E23',
    )

    WaitForThreadExit(0x000A, 0x0000)

    Jump('loc_3E36')

    def _loc_3E23(): pass

    label('loc_3E23')

    If(
        (
            (Expr.Eval, "OP_42(0x0F)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3E36',
    )

    WaitForThreadExit(0x000B, 0x0000)

    def _loc_3E36(): pass

    label('loc_3E36')

    WaitForThreadExit(0x00F8, 0x0000)
    def _loc_3E3B(): pass

    label('loc_3E3B')

    Jump('loc_3EAF')

    def _loc_3E3E(): pass

    label('loc_3E3E')

    ClearChrFlags(0x00F8, 0x0080)
    ClearChrFlags(0x00F9, 0x0080)
    SetChrPos(0x00F8, -21540, 200, 4840, 45)
    SetChrPos(0x00F9, -21540, 200, 4840, 45)

    @scena.Lambda('lambda_3E70')
    def lambda_3E70():
        OP_8F(0x00FE, -11140, 200, 9980, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_3E70)

    Sleep(300)

    @scena.Lambda('lambda_3E90')
    def lambda_3E90():
        OP_8F(0x00FE, -12010, 200, 10920, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_3E90)

    WaitForThreadExit(0x00F8, 0x0001)
    WaitForThreadExit(0x00F9, 0x0001)
    def _loc_3EAF(): pass

    label('loc_3EAF')

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3EE6',
    )

    ChrTalk(
        0x0107,
        (
            '#0070420946V#065F#6P姐姐！哥哥！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_40D7')

    def _loc_3EE6(): pass

    label('loc_3EE6')

    If(
        (
            (Expr.Eval, "OP_42(0x0A)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3F25',
    )

    ChrTalk(
        0x010B,
        (
            '#0090420947V#214F#6P约修亚！　艾丝蒂尔！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_40D7')

    def _loc_3F25(): pass

    label('loc_3F25')

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3F65',
    )

    ChrTalk(
        0x0105,
        (
            '#0060420948V#1163F#6P艾丝蒂尔！　约修亚！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_40D7')

    def _loc_3F65(): pass

    label('loc_3F65')

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3FA4',
    )

    ChrTalk(
        0x0103,
        (
            '#0030420949V#024F#6P艾丝蒂尔！　约修亚！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_40D7')

    def _loc_3FA4(): pass

    label('loc_3FA4')

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3FE3',
    )

    ChrTalk(
        0x0104,
        (
            '#0040420950V#530F#6P艾丝蒂尔！　约修亚！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_40D7')

    def _loc_3FE3(): pass

    label('loc_3FE3')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4022',
    )

    ChrTalk(
        0x0106,
        (
            '#0050420951V#054F#6P艾丝蒂尔！　约修亚！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_40D7')

    def _loc_4022(): pass

    label('loc_4022')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4061',
    )

    ChrTalk(
        0x0108,
        (
            '#0080420952V#076F#6P艾丝蒂尔！　约修亚！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_40D7')

    def _loc_4061(): pass

    label('loc_4061')

    If(
        (
            (Expr.Eval, "OP_42(0x0E)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_409D',
    )

    ChrTalk(
        0x010F,
        (
            '#0100420953V#177F艾丝蒂尔！　约修亚！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_40D7')

    def _loc_409D(): pass

    label('loc_409D')

    If(
        (
            (Expr.Eval, "OP_42(0x0F)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_40D7',
    )

    ChrTalk(
        0x0110,
        (
            '#0110420954V#271F<FIXME>……２人とも！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_40D7(): pass

    label('loc_40D7')

    If(
        (
            (Expr.Eval, "OP_42(0x08)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4185',
    )

    If(
        (
            (Expr.Eval, "OP_42(0x0E)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4138',
    )

    ChrTalk(
        0x000B,
        (
            '#0100420955V#177F#5P<FIXME>時間がない！\n',
            'とにかく急いでくれ！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4182')

    def _loc_4138(): pass

    label('loc_4138')

    If(
        (
            (Expr.Eval, "OP_42(0x0F)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4182',
    )

    ChrTalk(
        0x000A,
        (
            '#0110420956V#271F#5P<FIXME>時間がない！\n',
            'とにかく急げ！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4182(): pass

    label('loc_4182')

    Jump('loc_43CB')

    def _loc_4185(): pass

    label('loc_4185')

    If(
        (
            (Expr.Eval, "OP_42(0x0F)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_41CF',
    )

    ChrTalk(
        0x0110,
        (
            '#0110420957V#271F<FIXME>時間がない！\n',
            'とにかく急げ！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_43CB')

    def _loc_41CF(): pass

    label('loc_41CF')

    If(
        (
            (Expr.Eval, "OP_42(0x0E)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_421F',
    )

    ChrTalk(
        0x010F,
        (
            '#0100420958V#177F<FIXME>時間がない！\n',
            'とにかく急いでくれ！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_43CB')

    def _loc_421F(): pass

    label('loc_421F')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4263',
    )

    ChrTalk(
        0x0108,
        (
            '#0080420959V#076F#6P已经没有时间了！\n',
            '快一点！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_43CB')

    def _loc_4263(): pass

    label('loc_4263')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_42AB',
    )

    ChrTalk(
        0x0106,
        (
            '#0050420960V#054F#6P已经没有时间了！\n',
            '快跟上来啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_43CB')

    def _loc_42AB(): pass

    label('loc_42AB')

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_42EF',
    )

    ChrTalk(
        0x0104,
        (
            '#0040420961V#530F#6P已经没有时间了！\n',
            '快一点！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_43CB')

    def _loc_42EF(): pass

    label('loc_42EF')

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4337',
    )

    ChrTalk(
        0x0103,
        (
            '#0030420962V#024F#6P已经没有时间了啊！\n',
            '请快一点！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_43CB')

    def _loc_4337(): pass

    label('loc_4337')

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4382',
    )

    ChrTalk(
        0x0105,
        (
            '#0060420963V#1163F#6P没有时间了！\n',
            '……快一点啊……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_43CB')

    def _loc_4382(): pass

    label('loc_4382')

    If(
        (
            (Expr.Eval, "OP_42(0x0A)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_43CB',
    )

    ChrTalk(
        0x010B,
        (
            '#0090420964V#214F#6P时间不多了啊！\n',
            '再不快点的话……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_43CB(): pass

    label('loc_43CB')

    ClearChrFlags(0x0102, 0x0002)
    SetChrChipByIndex(0x0102, 65535)
    SetChrSubChip(0x0102, 0)

    @scena.Lambda('lambda_43E0')
    def lambda_43E0():
        OP_8C(0x00FE, 225, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_43E0)

    Sleep(100)

    ClearChrFlags(0x0102, 0x0002)
    SetChrChipByIndex(0x0102, 65535)
    SetChrSubChip(0x0102, 0)
    OP_8C(0x0102, 135, 0)
    OP_8C(0x0102, 225, 400)

    ChrTalk(
        0x0101,
        (
            '#0010420965V#1002F#2P嗯、嗯……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4442',
    )

    OP_A2(0x0006)

    def _loc_4442(): pass

    label('loc_4442')

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4453',
    )

    OP_A2(0x0006)

    def _loc_4453(): pass

    label('loc_4453')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4464',
    )

    OP_A2(0x0006)

    def _loc_4464(): pass

    label('loc_4464')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4475',
    )

    OP_A2(0x0006)

    def _loc_4475(): pass

    label('loc_4475')

    If(
        (
            (Expr.Eval, "OP_42(0x08)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4486',
    )

    OP_A2(0x0006)

    def _loc_4486(): pass

    label('loc_4486')

    If(
        (
            (Expr.Eval, "OP_42(0x0E)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4497',
    )

    OP_A2(0x0006)

    def _loc_4497(): pass

    label('loc_4497')

    If(
        (
            (Expr.Eval, "OP_42(0x0F)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_44A8',
    )

    OP_A2(0x0006)

    def _loc_44A8(): pass

    label('loc_44A8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_44E0',
    )

    ChrTalk(
        0x0102,
        (
            '#0020420966V#1035F#5P抱歉……马上出发。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4513')

    def _loc_44E0(): pass

    label('loc_44E0')

    ChrTalk(
        0x0102,
        (
            '#0020420967V#1035F#5P对不起……我们现在就走。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4513(): pass

    label('loc_4513')

    @scena.Lambda('lambda_4519')
    def lambda_4519():
        OP_6D(-8119, 200, 13830, 1800)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_4519)

    OP_8C(0x0102, 135, 300)
    SetChrFlags(0x0102, 0x0002)
    SetChrChipByIndex(0x0102, 2)
    SetChrSubChip(0x0102, 17)

    @scena.Lambda('lambda_4547')
    def lambda_4547():
        OP_8C(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_4547)

    OP_99(0x0102, 0x11, 0x13, 0x000003E8)
    WaitForThreadExit(0x0102, 0x0001)

    ChrTalk(
        0x0102,
        (
            '#0020420968V#1035F#6P（………………………………）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020420969V#1041F#6P（再见了……莱维。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(2000, 0, -1)
    OP_0D()
    OP_20(0x00000BB8)
    OP_24(0x0085, 0x46)
    Sleep(200)

    OP_24(0x0085, 0x3C)
    Sleep(200)

    OP_24(0x0085, 0x32)
    Sleep(200)

    OP_24(0x0085, 0x28)
    Sleep(200)

    OP_24(0x0085, 0x1E)
    Sleep(200)

    OP_24(0x0085, 0x14)
    Sleep(200)

    OP_24(0x0085, 0x0A)
    Sleep(200)

    OP_23(0x0085)
    OP_21()
    OP_A2(0x10F0)
    NewScene('ED6_DT21/C5300._SN', 107, 0, 0)
    IdleLoop()

    Return()

# id: 0x0003 offset: 0x461F
@scena.Code('func_03_461F')
def func_03_461F():
    OP_7C(0x00000046, 0x00000046, 0x000003E8, 0x000003E8)
    Sleep(1000)

    def _loc_4635(): pass

    label('loc_4635')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_4657',
    )

    OP_7C(0x00000028, 0x00000028, 0x000003E8, 0x000003E8)
    Sleep(1800)

    Jump('loc_4635')

    def _loc_4657(): pass

    label('loc_4657')

    Return()

# id: 0x0004 offset: 0x4658
@scena.Code('func_04_4658')
def func_04_4658():
    OP_8E(0x00FE, -1360, 3200, 60, 6000, 0x00)
    OP_8E(0x00FE, -7360, 200, 300, 6000, 0x00)
    OP_8E(0x00FE, -9580, 200, 12900, 6000, 0x00)
    OP_8C(0x00FE, 45, 600)
    SetChrFlags(0x00FE, 0x0002)
    SetChrChipByIndex(0x00FE, 1)
    SetChrSubChip(0x00FE, 0)
    OP_99(0x00FE, 0x00, 0x03, 0x000009C4)

    Return()

# id: 0x0005 offset: 0x46B4
@scena.Code('func_05_46B4')
def func_05_46B4():
    OP_8E(0x00FE, -1360, 3200, 60, 5000, 0x00)
    OP_8E(0x00FE, -7360, 200, 300, 5000, 0x00)
    OP_8E(0x00FE, -8470, 200, 9980, 5000, 0x00)
    OP_8C(0x00FE, 315, 400)

    Return()

# id: 0x0006 offset: 0x46F8
@scena.Code('func_06_46F8')
def func_06_46F8():
    OP_8E(0x00FE, -7910, 200, -890, 5000, 0x00)
    OP_8E(0x00FE, -8330, 200, 8350, 5000, 0x00)
    OP_8C(0x00FE, 315, 400)

    Return()

# id: 0x0007 offset: 0x4728
@scena.Code('func_07_4728')
def func_07_4728():
    OP_8E(0x00FE, -7260, 200, 1180, 5000, 0x00)
    OP_8E(0x00FE, -7260, 200, 9510, 5000, 0x00)
    OP_8C(0x00FE, 315, 400)

    Return()

# id: 0x0008 offset: 0x4758
@scena.Code('func_08_4758')
def func_08_4758():
    OP_8C(0x00FE, 253, 600)
    OP_8F(0x00FE, -20000, 100, 900, 5000, 0x00)
    SetChrFlags(0x0109, 0x0080)

    Return()

# id: 0x0009 offset: 0x4779
@scena.Code('func_09_4779')
def func_09_4779():
    ClearChrFlags(0x00FE, 0x0080)
    SetChrPos(0x00FE, -21540, 200, 4840, 45)

    @scena.Lambda('lambda_4795')
    def lambda_4795():
        OP_8F(0x00FE, -12010, 200, 10920, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_4795)

    WaitForThreadExit(0x00FE, 0x0001)

    Return()

# id: 0x000A offset: 0x47B0
@scena.Code('func_0A_47B0')
def func_0A_47B0():
    ClearChrFlags(0x000B, 0x0080)
    SetChrPos(0x000B, -21540, 200, 4840, 45)
    SetChrChipByIndex(0x000B, 19)

    @scena.Lambda('lambda_47D1')
    def lambda_47D1():
        OP_8F(0x00FE, -11140, 200, 9980, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_47D1)

    WaitForThreadExit(0x000B, 0x0001)
    SetChrChipByIndex(0x000B, 18)
    SetChrSubChip(0x000B, 0)

    Return()

# id: 0x000B offset: 0x47F6
@scena.Code('func_0B_47F6')
def func_0B_47F6():
    ClearChrFlags(0x000A, 0x0080)
    SetChrPos(0x000A, -21540, 200, 4840, 45)
    SetChrChipByIndex(0x000A, 21)

    @scena.Lambda('lambda_4817')
    def lambda_4817():
        OP_8F(0x00FE, -11140, 200, 9980, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_4817)

    WaitForThreadExit(0x000A, 0x0001)
    SetChrChipByIndex(0x000A, 20)
    SetChrSubChip(0x000A, 0)

    Return()

# id: 0x000C offset: 0x483C
@scena.Code('func_0C_483C')
def func_0C_483C():
    ClearChrFlags(0x00FE, 0x0080)
    SetChrPos(0x00FE, -21540, 200, 4840, 45)

    @scena.Lambda('lambda_4858')
    def lambda_4858():
        OP_8F(0x00FE, -11140, 200, 9980, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_4858)

    WaitForThreadExit(0x00FE, 0x0001)

    Return()

# id: 0x000D offset: 0x4873
@scena.Code('func_0D_4873')
def func_0D_4873():
    ClearChrFlags(0x000B, 0x0080)
    SetChrPos(0x000B, -21540, 200, 4840, 45)
    SetChrChipByIndex(0x000B, 19)

    @scena.Lambda('lambda_4894')
    def lambda_4894():
        OP_8F(0x00FE, -12010, 200, 10920, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_4894)

    WaitForThreadExit(0x000B, 0x0001)
    SetChrChipByIndex(0x000B, 18)
    SetChrSubChip(0x000B, 0)

    Return()

# id: 0x000E offset: 0x48B9
@scena.Code('func_0E_48B9')
def func_0E_48B9():
    ClearChrFlags(0x000A, 0x0080)
    SetChrPos(0x000A, -21540, 200, 4840, 45)
    SetChrChipByIndex(0x000A, 21)

    @scena.Lambda('lambda_48DA')
    def lambda_48DA():
        OP_8F(0x00FE, -12010, 200, 10920, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_48DA)

    WaitForThreadExit(0x000A, 0x0001)
    SetChrChipByIndex(0x000A, 20)
    SetChrSubChip(0x000A, 0)

    Return()

# id: 0x000F offset: 0x48FF
@scena.Code('func_0F_48FF')
def func_0F_48FF():
    SetChrPos(0x00FE, -7380, 200, 5270, 0)
    OP_8E(0x00FE, -4340, 200, 13910, 5000, 0x00)
    ChrTurnDirection(0x00FE, 0x0009, 0)

    Return()

# id: 0x0010 offset: 0x492C
@scena.Code('func_10_492C')
def func_10_492C():
    SetChrPos(0x00FE, -7380, 200, 5270, 0)
    OP_8E(0x00FE, -5500, 200, 14430, 5000, 0x00)
    ChrTurnDirection(0x00FE, 0x0009, 0)

    Return()

# id: 0x0011 offset: 0x4959
@scena.Code('func_11_4959')
def func_11_4959():
    Sleep(500)

    SetChrPos(0x00F8, -7380, 200, 5270, 0)
    SetChrPos(0x00F9, -7380, 200, 5270, 0)

    If(
        (
            (Expr.Eval, "OP_42(0x08)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4A03',
    )

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_49CF',
    )

    OP_8E(0x00F9, -6420, 200, 14880, 5000, 0x00)
    ChrTurnDirection(0x00F9, 0x0009, 400)
    SetChrFlags(0x0109, 0x0080)
    SetChrPos(0x0109, -50000, -50000, -50000, 0)

    Jump('loc_4A00')

    def _loc_49CF(): pass

    label('loc_49CF')

    OP_8E(0x00F8, -6420, 200, 14880, 5000, 0x00)
    ChrTurnDirection(0x00F8, 0x0009, 400)
    SetChrFlags(0x0109, 0x0080)
    SetChrPos(0x0109, -50000, -50000, -50000, 0)

    def _loc_4A00(): pass

    label('loc_4A00')

    Jump('loc_4A56')

    def _loc_4A03(): pass

    label('loc_4A03')

    @scena.Lambda('lambda_4A09')
    def lambda_4A09():
        OP_8E(0x00FE, -6420, 200, 14880, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_4A09)

    Sleep(500)

    @scena.Lambda('lambda_4A29')
    def lambda_4A29():
        OP_8E(0x00FE, -3570, 200, 13350, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_4A29)

    WaitForThreadExit(0x00F9, 0x0001)
    ChrTurnDirection(0x00F9, 0x0009, 400)
    WaitForThreadExit(0x00F8, 0x0001)
    ChrTurnDirection(0x00F8, 0x0009, 400)
    def _loc_4A56(): pass

    label('loc_4A56')

    Return()

# id: 0x0012 offset: 0x4A57
@scena.Code('func_12_4A57')
def func_12_4A57():
    SetChrFlags(0x00FE, 0x0040)
    ClearChrFlags(0x00FE, 0x0080)
    SetChrPos(0x00FE, -21630, 200, -350, 45)
    OP_8E(0x00FE, -10550, 200, 7500, 5000, 0x00)
    SetChrChipByIndex(0x00FE, 18)
    SetChrSubChip(0x00FE, 0)

    Return()

# id: 0x0013 offset: 0x4A91
@scena.Code('func_13_4A91')
def func_13_4A91():
    SetChrFlags(0x00FE, 0x0040)
    ClearChrFlags(0x00FE, 0x0080)
    SetChrPos(0x00FE, -21260, 200, 2100, 45)
    OP_8E(0x00FE, -11460, 200, 8760, 5000, 0x00)
    SetChrChipByIndex(0x00FE, 20)
    SetChrSubChip(0x00FE, 0)

    Return()

# id: 0x0014 offset: 0x4ACB
@scena.Code('func_14_4ACB')
def func_14_4ACB():
    SetChrFlags(0x00FE, 0x0040)
    ClearChrFlags(0x00FE, 0x0080)
    SetChrPos(0x00FE, -21630, 200, -350, 45)
    OP_8E(0x00FE, -11990, 200, 6140, 5000, 0x00)
    SetChrChipByIndex(0x00FE, 27)
    SetChrSubChip(0x00FE, 0)

    Return()

# id: 0x0015 offset: 0x4B05
@scena.Code('func_15_4B05')
def func_15_4B05():
    SetChrFlags(0x00FE, 0x0040)
    ClearChrFlags(0x00FE, 0x0080)
    SetChrPos(0x00FE, -21630, 200, -350, 45)
    OP_8E(0x00FE, -11310, 200, 5080, 5000, 0x00)
    SetChrChipByIndex(0x00FE, 29)
    SetChrSubChip(0x00FE, 0)

    Return()

# id: 0x0016 offset: 0x4B3F
@scena.Code('func_16_4B3F')
def func_16_4B3F():
    SetChrFlags(0x00FE, 0x0040)
    ClearChrFlags(0x00FE, 0x0080)
    SetChrPos(0x00FE, -21630, 200, -350, 45)
    OP_8E(0x00FE, -12640, 200, 7450, 5000, 0x00)
    SetChrChipByIndex(0x00FE, 31)
    SetChrSubChip(0x00FE, 0)

    Return()

# id: 0x0017 offset: 0x4B79
@scena.Code('func_17_4B79')
def func_17_4B79():
    SetChrFlags(0x00FE, 0x0040)
    ClearChrFlags(0x00FE, 0x0080)
    SetChrPos(0x00FE, -21910, 200, 280, 45)
    OP_8E(0x00FE, -13680, 200, 7420, 5000, 0x00)
    SetChrChipByIndex(0x00FE, 33)
    SetChrSubChip(0x00FE, 0)

    Return()

# id: 0x0018 offset: 0x4BB3
@scena.Code('func_18_4BB3')
def func_18_4BB3():
    SetChrFlags(0x00FE, 0x0040)
    ClearChrFlags(0x00FE, 0x0080)
    SetChrPos(0x00FE, -21630, 200, -350, 45)
    OP_8E(0x00FE, -12530, 200, 3700, 5000, 0x00)
    SetChrChipByIndex(0x00FE, 35)
    SetChrSubChip(0x00FE, 0)

    Return()

# id: 0x0019 offset: 0x4BED
@scena.Code('func_19_4BED')
def func_19_4BED():
    SetChrFlags(0x00FE, 0x0040)
    ClearChrFlags(0x00FE, 0x0080)
    SetChrPos(0x00FE, -21910, 200, 280, 45)
    OP_8E(0x00FE, -14790, 200, 6010, 5000, 0x00)
    SetChrChipByIndex(0x00FE, 37)
    SetChrSubChip(0x00FE, 0)

    Return()

# id: 0x001A offset: 0x4C27
@scena.Code('func_1A_4C27')
def func_1A_4C27():
    SetChrFlags(0x00FE, 0x0040)
    ClearChrFlags(0x00FE, 0x0080)
    SetChrPos(0x00FE, -21630, 200, -350, 45)
    OP_8E(0x00FE, -13030, 200, 5830, 5000, 0x00)

    Return()

# id: 0x001B offset: 0x4C57
@scena.Code('func_1B_4C57')
def func_1B_4C57():
    SetChrFlags(0x00FE, 0x0040)
    ClearChrFlags(0x00FE, 0x0080)
    SetChrPos(0x00FE, -21910, 200, 280, 45)
    OP_8E(0x00FE, -13570, 200, 3820, 5000, 0x00)
    SetChrChipByIndex(0x00FE, 25)
    SetChrSubChip(0x00FE, 0)

    Return()

# id: 0x001C offset: 0x4C91
@scena.Code('func_1C_4C91')
def func_1C_4C91():
    SetChrFlags(0x00FE, 0x0040)
    ClearChrFlags(0x00FE, 0x0080)
    SetChrPos(0x00FE, -21630, 200, -350, 45)
    OP_8E(0x00FE, -14530, 200, 4340, 5000, 0x00)
    SetChrChipByIndex(0x00FE, 23)
    SetChrSubChip(0x00FE, 0)

    Return()

# id: 0x001D offset: 0x4CCB
@scena.Code('func_1D_4CCB')
def func_1D_4CCB():
    OP_8C(0x00FE, 270, 400)
    SetChrChipByIndex(0x00FE, 19)
    OP_8E(0x00FE, -21280, 200, -500, 5000, 0x00)
    OP_8E(0x00FE, -55280, 200, -500, 5000, 0x00)
    SetChrFlags(0x00FE, 0x0080)

    Return()

# id: 0x001E offset: 0x4D05
@scena.Code('func_1E_4D05')
def func_1E_4D05():
    OP_8C(0x00FE, 270, 400)
    SetChrChipByIndex(0x00FE, 21)
    OP_8E(0x00FE, -21440, 200, 1210, 5000, 0x00)
    OP_8E(0x00FE, -55440, 200, 1210, 5000, 0x00)
    SetChrFlags(0x00FE, 0x0080)

    Return()

# id: 0x001F offset: 0x4D3F
@scena.Code('func_1F_4D3F')
def func_1F_4D3F():
    OP_8C(0x00FE, 270, 400)
    SetChrChipByIndex(0x00FE, 28)
    OP_8E(0x00FE, -22620, 200, 670, 5000, 0x00)
    OP_8E(0x00FE, -55350, 200, -220, 5000, 0x00)
    SetChrFlags(0x00FE, 0x0080)

    Return()

# id: 0x0020 offset: 0x4D79
@scena.Code('func_20_4D79')
def func_20_4D79():
    OP_8C(0x00FE, 270, 400)
    SetChrChipByIndex(0x00FE, 30)
    OP_8E(0x00FE, -21350, 200, -160, 5000, 0x00)
    OP_8E(0x00FE, -55800, 200, -610, 5000, 0x00)
    SetChrFlags(0x00FE, 0x0080)

    Return()

# id: 0x0021 offset: 0x4DB3
@scena.Code('func_21_4DB3')
def func_21_4DB3():
    OP_8C(0x00FE, 270, 400)
    SetChrChipByIndex(0x00FE, 32)
    OP_8E(0x00FE, -21870, 200, 1600, 5000, 0x00)
    OP_8E(0x00FE, -55350, 200, 550, 5000, 0x00)
    SetChrFlags(0x00FE, 0x0080)

    Return()

# id: 0x0022 offset: 0x4DED
@scena.Code('func_22_4DED')
def func_22_4DED():
    OP_8C(0x00FE, 270, 400)
    SetChrChipByIndex(0x00FE, 34)
    OP_8E(0x00FE, -22420, 200, 1360, 5000, 0x00)
    OP_8E(0x00FE, -55670, 200, 1050, 5000, 0x00)
    SetChrFlags(0x00FE, 0x0080)

    Return()

# id: 0x0023 offset: 0x4E27
@scena.Code('func_23_4E27')
def func_23_4E27():
    OP_8C(0x00FE, 270, 400)
    SetChrChipByIndex(0x00FE, 36)
    OP_8E(0x00FE, -22560, 200, -200, 5000, 0x00)
    OP_8E(0x00FE, -55610, 200, 1470, 5000, 0x00)
    SetChrFlags(0x00FE, 0x0080)

    Return()

# id: 0x0024 offset: 0x4E61
@scena.Code('func_24_4E61')
def func_24_4E61():
    OP_8C(0x00FE, 270, 400)
    SetChrChipByIndex(0x00FE, 38)
    OP_8E(0x00FE, -23020, 200, 940, 5000, 0x00)
    OP_8E(0x00FE, -55010, 200, 2210, 5000, 0x00)
    SetChrFlags(0x00FE, 0x0080)

    Return()

# id: 0x0025 offset: 0x4E9B
@scena.Code('func_25_4E9B')
def func_25_4E9B():
    OP_8C(0x00FE, 270, 400)
    OP_8E(0x00FE, -23350, 180, -630, 5000, 0x00)
    OP_8E(0x00FE, -55830, 200, 1100, 5000, 0x00)
    SetChrFlags(0x00FE, 0x0080)

    Return()

# id: 0x0026 offset: 0x4ED0
@scena.Code('func_26_4ED0')
def func_26_4ED0():
    OP_8C(0x00FE, 270, 400)
    SetChrChipByIndex(0x00FE, 26)
    OP_8E(0x00FE, -23170, 190, 470, 5000, 0x00)
    OP_8E(0x00FE, -55510, 200, -2060, 5000, 0x00)
    SetChrFlags(0x00FE, 0x0080)

    Return()

# id: 0x0027 offset: 0x4F0A
@scena.Code('func_27_4F0A')
def func_27_4F0A():
    OP_8C(0x00FE, 270, 400)
    SetChrChipByIndex(0x00FE, 24)
    OP_8E(0x00FE, -23650, 170, 1000, 5000, 0x00)
    OP_8E(0x00FE, -55860, 200, -1140, 5000, 0x00)
    SetChrFlags(0x00FE, 0x0080)

    Return()

# id: 0x0028 offset: 0x4F44
@scena.Code('func_28_4F44')
def func_28_4F44():
    OP_8C(0x00FE, 270, 400)
    OP_8E(0x00FE, -22600, 200, -1310, 5000, 0x00)
    OP_8E(0x00FE, -55600, 200, -1310, 5000, 0x00)
    SetChrFlags(0x00FE, 0x0080)

    Return()

# id: 0x0029 offset: 0x4F79
@scena.Code('func_29_4F79')
def func_29_4F79():
    OP_8C(0x00FE, 270, 400)
    OP_8E(0x00FE, -21730, 200, 580, 5000, 0x00)
    OP_8E(0x00FE, -55730, 200, 580, 5000, 0x00)
    SetChrFlags(0x00FE, 0x0080)

    Return()

# id: 0x002A offset: 0x4FAE
@scena.Code('func_2A_4FAE')
def func_2A_4FAE():
    OP_24(0x0144, 0x5A)
    Sleep(300)

    OP_24(0x0144, 0x50)
    Sleep(300)

    OP_24(0x0144, 0x46)
    Sleep(300)

    OP_24(0x0144, 0x3C)
    Sleep(300)

    OP_24(0x0144, 0x32)
    Sleep(300)

    OP_24(0x0144, 0x28)
    Sleep(300)

    OP_24(0x0144, 0x1E)
    Sleep(300)

    OP_24(0x0144, 0x14)
    Sleep(300)

    OP_23(0x0144)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
